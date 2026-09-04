"""
SlateGate — Content Greenlight Agent Backend.
FastAPI Application Entrypoint.
"""

import logging
from contextlib import asynccontextmanager
from typing import Any, Dict, List, Optional

from fastapi import FastAPI, HTTPException, Query, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles

from app.agent.launch_director import LaunchDirectorAgent
from app.config import settings
from app.engine.fixtures import TITLES_FIXTURE
from app.mcp.client import McpQueryError, McpTimeoutError
from app.models.request import GreenlightRequest, RemediationRequest
from app.models.response import (
    FleetAnalyticsResponse,
    GreenlightResponse,
    RemediationResponse,
)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger("slategate")


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting SlateGate Content Greenlight Agent service...")
    logger.info(f"ClickHouse Live Configured: {settings.has_clickhouse_credentials}")
    logger.info(f"Gemini AI Configured: {settings.has_gemini_credentials} (Model: {settings.gemini_model})")
    yield
    logger.info("Shutting down SlateGate service...")


app = FastAPI(
    title="SlateGate — Content Greenlight Agent",
    description="Deterministic Southeast Asian Content Greenlight Audit Agent powered by ClickHouse MCP & Google Gemini.",
    version="1.0.0",
    lifespan=lifespan,
)

# CORS middleware for development flexibility
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Shared agent instance
agent = LaunchDirectorAgent()


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/health", summary="Service Health Check")
async def health_check() -> Dict[str, Any]:
    """Health check endpoint for container orchestrators (Google Cloud Run)."""
    return {
        "status": "healthy",
        "service": "slategate",
        "version": "1.0.0",
        "environment": settings.app_env,
        "clickhouse_configured": settings.has_clickhouse_credentials,
        "gemini_configured": settings.has_gemini_credentials,
        "gemini_model": settings.gemini_model,
        "default_mode": settings.default_data_mode,
    }


@app.get("/api/scenarios", summary="Get Preset Fictional Scenarios")
async def get_scenarios() -> List[Dict[str, Any]]:
    """Returns preset fictional scenarios for one-click UI evaluation."""
    scenarios = [
        {
            "id": "slate-001",
            "title": "The Nusantara Heist",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "expected_decision": "RED",
            "description": "Thailand rights window expired (2026-06-30); Indonesian subtitle missing; Thai artwork missing.",
        },
        {
            "id": "slate-002",
            "title": "Singa City Beats",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "expected_decision": "GREEN",
            "description": "Active rights through 2028 and all QC-passed deliverables present in ID, TH, and SG.",
        },
        {
            "id": "slate-003",
            "title": "Bangkok Neon Nights",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "expected_decision": "RED",
            "description": "Indonesian master video failed broadcast audio loudness QC (-18.2 LUFS).",
        },
        {
            "id": "slate-004",
            "title": "Java Horizon",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "expected_decision": "AMBER",
            "description": "Rights and master videos valid; Bahasa Indonesia subtitle track missing in asset catalog.",
        },
    ]
    return scenarios


@app.post(
    "/api/greenlight",
    response_model=GreenlightResponse,
    summary="Evaluate Content Greenlight",
    responses={
        200: {"description": "Greenlight decision successfully evaluated."},
        422: {"description": "Validation error in request parameters."},
        502: {"description": "ClickHouse MCP query execution failure."},
        504: {"description": "ClickHouse MCP query timed out."},
    },
)
async def evaluate_greenlight_endpoint(request: GreenlightRequest) -> GreenlightResponse:
    """
    Evaluates launch readiness for a given title, launch date, target territories, and platform.
    """
    try:
        response = await agent.execute_audit(request)
        return response
    except McpTimeoutError as e:
        logger.error(f"MCP Timeout Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_504_GATEWAY_TIMEOUT,
            detail={
                "error": "clickhouse_timeout",
                "message": str(e),
                "decision": "error",
            },
        )
    except McpQueryError as e:
        logger.error(f"MCP Query Error: {e}")
        raise HTTPException(
            status_code=status.HTTP_502_BAD_GATEWAY,
            detail={
                "error": "clickhouse_error",
                "message": str(e),
                "decision": "error",
            },
        )
    except Exception as e:
        logger.exception(f"Unexpected internal error during greenlight evaluation: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={
                "error": "internal_error",
                "message": f"Unexpected error during greenlight audit: {e}",
            },
        )


@app.get(
    "/api/analytics/fleet",
    response_model=FleetAnalyticsResponse,
    summary="Get Fleet-Wide OLAP Analytics (ClickHouse Aggregations)",
)
async def get_fleet_analytics_endpoint(
    mode: Optional[str] = Query(default=None, description="Override data mode ('clickhouse-mcp' or 'fixture')"),
) -> FleetAnalyticsResponse:
    """
    Executes high-performance ClickHouse OLAP aggregation queries across the studio catalog.
    Computes territory readiness rates, bottleneck breakdown, and technical QC pass rates.
    """
    try:
        analytics = await agent.mcp_client.fetch_fleet_analytics(force_data_mode=mode)
        return analytics
    except Exception as e:
        logger.exception(f"Fleet analytics query failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "fleet_analytics_error", "message": str(e)},
        )


@app.post(
    "/api/remediate",
    response_model=RemediationResponse,
    summary="Generate Agentic Remediation Work Order (Gemini Media Copilot)",
)
async def remediate_issue_endpoint(request: RemediationRequest) -> RemediationResponse:
    """
    Uses Google Gemini Launch Director to transform diagnostic check failures
    into production-ready operational work orders, FFmpeg audio loudness transcode commands,
    or formal licensing addendum draft notices.
    """
    try:
        work_order = await agent.generate_remediation_work_order(request)
        return work_order
    except Exception as e:
        logger.exception(f"Remediation generation failed: {e}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail={"error": "remediation_error", "message": str(e)},
        )


# Mount static files for control room frontend
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", include_in_schema=False)
async def serve_index():
    """Serve the single-page operational control room."""
    return FileResponse("app/static/index.html")
