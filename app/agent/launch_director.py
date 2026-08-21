"""
Google ADK & Gemini Launch Director Agent.
Orchestrates the Content Greenlight audit flow using official Google AI tools (Google GenAI / ADK),
queries ClickHouse via MCP, evaluates deterministic policies, and synthesizes executive summaries.
"""

import json
import logging
from datetime import date
from typing import Any, Dict, List, Optional

from app.config import settings
from app.engine.policy import evaluate_greenlight
from app.mcp.client import ClickHouseMcpClient
from app.models.request import GreenlightRequest
from app.models.response import GreenlightResponse

logger = logging.getLogger("slategate.agent")


LAUNCH_DIRECTOR_SYSTEM_INSTRUCTION = """
You are the Executive Launch Director for SlateGate, a Southeast Asian media distribution operations system.
Your mission is to analyze content greenlight audit data (rights windows, technical QC, localization, artwork, metadata)
and provide clear, concise, authoritative launch summaries for regional operations teams.

CRITICAL POLICY RULES:
1. You MUST NEVER override the deterministic decision (RED, AMBER, GREEN).
2. RED means launch is strictly BLOCKED due to expired/conflicting rights or failed/missing master video.
3. AMBER means launch is CONDITIONALLY APPROVED pending non-critical supporting deliverables (subtitles, artwork, metadata).
4. GREEN means launch is FULLY APPROVED across all requested territories.
5. In your summary, state the decision clearly in the first sentence, name the specific territory and blocker, identify the responsible department owner, and prescribe the required next action. Keep your summary under 3 sentences.
""".strip()


class LaunchDirectorAgent:
    """
    Launch Director Agent powered by Google ADK / Google GenAI SDK and Gemini Flash.
    """

    def __init__(self, mcp_client: Optional[ClickHouseMcpClient] = None):
        self.mcp_client = mcp_client or ClickHouseMcpClient()
        self.model_name = settings.gemini_model
        self.api_key = settings.gemini_api_key
        self.project = settings.google_cloud_project
        self.location = settings.google_cloud_location

    def is_gemini_configured(self) -> bool:
        """Check if Google AI / Vertex credentials are present."""
        return settings.has_gemini_credentials

    async def execute_audit(self, request: GreenlightRequest) -> GreenlightResponse:
        """
        Runs the full audit lifecycle:
        1. Fetch analytical data through ClickHouse MCP client.
        2. Evaluate deterministic decision policy and itemized checks.
        3. Invoke Gemini Launch Director for executive synthesis (if credentials available).
        4. Package evidence-backed response with real tool trace.
        """
        # Step 1: Query analytical storage via ClickHouse MCP / Fixture
        raw_data, tool_trace, data_mode = await self.mcp_client.fetch_greenlight_data(
            title_id=request.title_id,
            launch_date=request.launch_date,
            territories=request.territories,
            platform=request.platform,
            force_data_mode=request.force_data_mode,
        )

        # Step 2: Evaluate pure deterministic policy
        response = evaluate_greenlight(
            title_id=request.title_id,
            launch_date=request.launch_date,
            territories=request.territories,
            platform=request.platform,
            raw_data=raw_data,
            tool_trace=tool_trace,
            data_mode=data_mode,
        )

        # Step 3: Google Gemini Launch Director Synthesis
        if self.is_gemini_configured():
            try:
                gemini_summary = await self._synthesize_with_gemini(request, response)
                if gemini_summary:
                    response.summary = gemini_summary
                    response.tool_trace.append("gemini.agent:launch_director")
            except Exception as e:
                logger.warning(f"Gemini agent synthesis skipped due to API error: {e}")
                # Fallback remains pure deterministic summary
                response.tool_trace.append("agent:launch_director")
        else:
            response.tool_trace.append("agent:launch_director")

        return response

    async def _synthesize_with_gemini(
        self,
        request: GreenlightRequest,
        response: GreenlightResponse,
    ) -> Optional[str]:
        """
        Invokes Gemini Flash using Google GenAI SDK to generate crisp executive synthesis.
        """
        try:
            # Dynamically import google.genai
            from google import genai
            from google.genai import types

            client_kwargs: Dict[str, Any] = {}
            if self.api_key:
                client_kwargs["api_key"] = self.api_key
            elif self.project:
                client_kwargs["vertexai"] = True
                client_kwargs["project"] = self.project
                client_kwargs["location"] = self.location

            client = genai.Client(**client_kwargs)

            # Prepare structured context for Gemini
            failing_checks = [c.model_dump() for c in response.checks if c.status != "pass"]
            prompt = f"""
            Analyze the following Greenlight Audit Result:
            - Title ID: {request.title_id}
            - Platform: {request.platform}
            - Launch Date: {request.launch_date}
            - Territories: {request.territories}
            - Deterministic Decision: {response.decision.value.upper()}
            - Passed Checks: {response.passed_count} / {response.total_count}
            - Failed Checks Summary: {json.dumps(failing_checks, indent=2)}

            Produce an executive summary (max 2-3 sentences) adhering strictly to the {response.decision.value.upper()} decision.
            """

            gen_response = await client.aio.models.generate_content(
                model=self.model_name,
                contents=prompt,
                config=types.GenerateContentConfig(
                    system_instruction=LAUNCH_DIRECTOR_SYSTEM_INSTRUCTION,
                    temperature=0.1,
                    max_output_tokens=256,
                ),
            )

            if gen_response and gen_response.text:
                return gen_response.text.strip()
        except ImportError:
            logger.info("google-genai package not installed or importable; using deterministic baseline.")
        except Exception as e:
            logger.warning(f"Error during Gemini call: {e}")

        return None
