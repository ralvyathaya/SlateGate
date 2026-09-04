"""
Google ADK & Gemini Launch Director Agent.
Orchestrates the Content Greenlight audit flow using official Google AI tools (Google GenAI / ADK),
queries ClickHouse via MCP, evaluates deterministic policies, and synthesizes executive summaries.
"""

import json
import logging
import time
import uuid
from datetime import date
from typing import Any, Dict, List, Optional

from app.config import settings
from app.engine.policy import evaluate_greenlight
from app.mcp.client import ClickHouseMcpClient
from app.models.request import GreenlightRequest, RemediationRequest
from app.models.response import GreenlightResponse, RemediationResponse

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
        audit_start = time.perf_counter()

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

        response.execution_time_ms = round((time.perf_counter() - audit_start) * 1000.0, 2)
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

    async def generate_remediation_work_order(self, req: RemediationRequest) -> RemediationResponse:
        """
        Generates an actionable operational work order or remediation script
        tailored to the specific check failure using Google Gemini.
        """
        action_id = f"rem-{uuid.uuid4().hex[:8]}"
        cat = req.category.lower()

        # Deterministic Baseline Configuration
        if "master" in cat:
            action_type = "ffmpeg_loudness_conformance"
            work_order_title = f"Broadcast Audio Loudness Normalization (EBU R128) - {req.title_id} ({req.territory})"
            work_order_content = (
                f"WORK ORDER: Technical Operations / Audio Conformance Unit\n"
                f"TITLE: {req.title_id} | TERRITORY: {req.territory}\n"
                f"DEFECT: {req.reason}\n\n"
                f"ACTION PROTOCOL:\n"
                f"1. Ingest existing broadcast master from repository.\n"
                f"2. Apply two-pass EBU R128 loudness correction filter with target integrated loudness -24.0 LUFS (±1.0 LUFS) and maximum true peak -2.0 dBFS.\n"
                f"3. Verify ProRes 422 HQ video stream integrity without re-encoding video essence.\n"
                f"4. Output conform master and update ClickHouse QC register."
            )
            cli_cmd = (
                f"ffmpeg -i input_master_{req.title_id}_{req.territory.lower()}.mov "
                f"-af loudnorm=I=-24.0:LRA=7.0:tp=-2.0 -c:v copy -c:a pcm_s24le "
                f"output_master_ebur128_{req.territory.lower()}.mov"
            )
            assigned_team = "Technical Operations & Audio Engineering"
            priority = "URGENT - LAUNCH BLOCKER"
            turnaround = "4 Hours"

        elif "rights" in cat:
            action_type = "licensing_addendum_memo"
            work_order_title = f"FAST Distribution Rights Window Extension Notice - {req.title_id} ({req.territory})"
            work_order_content = (
                f"LEGAL MEMORANDUM: Rights & Business Affairs\n"
                f"TITLE: {req.title_id} | TERRITORY: {req.territory}\n"
                f"CURRENT STATUS: {req.reason}\n"
                f"EVIDENCE: {', '.join(req.evidence)}\n\n"
                f"DRAFT ADDENDUM TERMS:\n"
                f"- Licensor: Southeast Asia Content Partners Ltd.\n"
                f"- Licensee: Regional FAST Operations Network\n"
                f"- Scope: Exercise Option Period 2 for territory '{req.territory}' across non-exclusive ad-supported streaming.\n"
                f"- Term: Retroactive extension from current lapse through 2028-12-31.\n"
                f"- Action: Transmit formal exercise notice to licensor representation within 24 business hours."
            )
            cli_cmd = None
            assigned_team = "Rights & Licensing / Business Affairs"
            priority = "URGENT - LAUNCH BLOCKER"
            turnaround = "24-48 Hours"

        elif "sub" in cat:
            action_type = "localization_dispatch_ticket"
            lang = "Bahasa Indonesia (id)" if req.territory == "ID" else "Thai (th)" if req.territory == "TH" else "English/Chinese (sg)"
            work_order_title = f"Expedited Subtitle Ingest & Alignment Order - {req.title_id} ({req.territory})"
            work_order_content = (
                f"LOCALIZATION DISPATCH: Regional Localization Hub\n"
                f"TITLE: {req.title_id} | TARGET LANGUAGE: {lang}\n"
                f"REQUIREMENT: {req.reason}\n\n"
                f"SPECIFICATIONS:\n"
                f"- Subtitle format: Localized SRT/VTT in UTF-8 encoding.\n"
                f"- Maximum line length: 37 characters; Maximum 2 lines per subtitle event.\n"
                f"- Reading speed ceiling: 17 characters per second (CPS).\n"
                f"- Timecode alignment: Conformed precisely to 24.000 fps master video essence."
            )
            cli_cmd = f"subpqc --validate --source master_{req.title_id}.mov --input sub_{req.territory.lower()}.srt --target-fps 24.0 --max-cps 17"
            assigned_team = "Localization Operations Hub"
            priority = "HIGH - PRE-LAUNCH DELIVERY"
            turnaround = "12 Hours"

        elif "art" in cat or "poster" in cat or "banner" in cat:
            action_type = "creative_ops_spec_ticket"
            work_order_title = f"Key Art Sizing & Localization Dispatch - {req.title_id} ({req.territory})"
            work_order_content = (
                f"CREATIVE BRIEF: Design & Key Art Delivery\n"
                f"TITLE: {req.title_id} | TERRITORY: {req.territory}\n"
                f"REQUIREMENT: {req.reason}\n\n"
                f"DELIVERABLE SPECS:\n"
                f"- Portrait Poster: 2000x3000 (2:3 aspect ratio), sRGB, max 5MB, localized title typography.\n"
                f"- Landscape Banner: 3840x2160 (16:9 aspect ratio), safe area margins 15% clear of title text."
            )
            cli_cmd = f"magick convert raw_poster.png -resize 2000x3000^ -gravity center -extent 2000x3000 -quality 95 poster_{req.territory.lower()}.jpg"
            assigned_team = "Creative Operations"
            priority = "MEDIUM"
            turnaround = "8 Hours"

        else:
            action_type = "metadata_compliance_submission"
            work_order_title = f"Regulatory Metadata & Classification Filing - {req.title_id} ({req.territory})"
            work_order_content = (
                f"REGULATORY SUBMISSION: Standards & Content Operations\n"
                f"TITLE: {req.title_id} | TERRITORY: {req.territory}\n"
                f"STATUS: {req.reason}\n\n"
                f"MANDATORY METADATA FIELDS:\n"
                f"- Localized Title & 250-character Synopsis\n"
                f"- Content Rating: Singapore IMDA / Indonesia LSF Certification\n"
                f"- Cast & Director Credits (in UTF-8 localized characters)"
            )
            cli_cmd = None
            assigned_team = "Content Operations & Standards"
            priority = "MEDIUM"
            turnaround = "8 Hours"

        tool_trace = ["agent:remediation_generator"]

        # Enhance with Gemini if available
        if self.is_gemini_configured():
            try:
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

                prompt = f"""
                You are the Lead Content Operations Director.
                Generate a professional, production-ready operational work order to resolve this launch blocker:
                - Title: {req.title_id}
                - Territory: {req.territory}
                - Issue Category: {req.category}
                - Issue Detail: {req.reason}
                - Evidence: {req.evidence}
                - Action Type: {action_type}

                Keep the response structured, authoritative, and actionable for studio engineers or legal staff.
                """

                gen_response = await client.aio.models.generate_content(
                    model=self.model_name,
                    contents=prompt,
                    config=types.GenerateContentConfig(
                        temperature=0.2,
                        max_output_tokens=350,
                    ),
                )
                if gen_response and gen_response.text:
                    work_order_content = gen_response.text.strip()
                    tool_trace.append("gemini.agent:remediation_generator")
            except Exception as e:
                logger.warning(f"Gemini remediation enhancement skipped: {e}")

        return RemediationResponse(
            remediation_id=action_id,
            title_id=req.title_id,
            territory=req.territory,
            category=req.category,
            action_type=action_type,
            work_order_title=work_order_title,
            work_order_content=work_order_content,
            cli_command=cli_cmd,
            assigned_team=assigned_team,
            priority=priority,
            estimated_turnaround=turnaround,
            tool_trace=tool_trace,
        )

