"""
Integration Tests for SlateGate FastAPI Endpoints.
"""

from unittest.mock import patch
import pytest
from httpx import ASGITransport, AsyncClient

from app.main import app
from app.mcp.client import McpQueryError, McpTimeoutError


@pytest.mark.asyncio
async def test_health_check_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/health")
        assert response.status_code == 200
        data = response.json()
        assert data["status"] == "healthy"
        assert data["service"] == "slategate"
        assert "clickhouse_configured" in data
        assert "gemini_configured" in data


@pytest.mark.asyncio
async def test_get_scenarios_endpoint():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/scenarios")
        assert response.status_code == 200
        data = response.json()
        assert len(data) == 4
        ids = [s["id"] for s in data]
        assert "slate-001" in ids
        assert "slate-002" in ids
        assert "slate-003" in ids
        assert "slate-004" in ids


@pytest.mark.asyncio
async def test_greenlight_slate_001_red():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-001",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "force_data_mode": "fixture"
        }
        response = await client.post("/api/greenlight", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["decision"] == "red"
        assert data["data_mode"] == "fixture"
        assert len(data["checks"]) > 0
        assert len(data["tool_trace"]) > 0


@pytest.mark.asyncio
async def test_greenlight_slate_002_green():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-002",
            "launch_date": "2026-09-15",
            "territories": ["ID", "TH", "SG"],
            "platform": "FAST",
            "force_data_mode": "fixture"
        }
        response = await client.post("/api/greenlight", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["decision"] == "green"
        assert data["failed_count"] == 0
        assert data["passed_count"] == data["total_count"]


@pytest.mark.asyncio
async def test_greenlight_invalid_territory_validation():
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-001",
            "launch_date": "2026-09-15",
            "territories": ["INVALID_TERRITORY"],
            "platform": "FAST"
        }
        response = await client.post("/api/greenlight", json=payload)
        assert response.status_code == 422


@pytest.mark.asyncio
async def test_greenlight_mcp_timeout_returns_http_504():
    """Verify that a ClickHouse MCP timeout returns HTTP 504 error, never a greenlight."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        with patch("app.mcp.client.ClickHouseMcpClient.fetch_greenlight_data", side_effect=McpTimeoutError("ClickHouse timed out")):
            payload = {
                "title_id": "slate-002",
                "launch_date": "2026-09-15",
                "territories": ["ID", "TH", "SG"],
                "platform": "FAST",
                "force_data_mode": "clickhouse-mcp"
            }
            response = await client.post("/api/greenlight", json=payload)
            assert response.status_code == 504
            data = response.json()
            assert "detail" in data
            assert data["detail"]["error"] == "clickhouse_timeout"


@pytest.mark.asyncio
async def test_greenlight_mcp_error_returns_http_502():
    """Verify that a ClickHouse MCP execution error returns HTTP 502 error."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        with patch("app.mcp.client.ClickHouseMcpClient.fetch_greenlight_data", side_effect=McpQueryError("Connection refused")):
            payload = {
                "title_id": "slate-002",
                "launch_date": "2026-09-15",
                "territories": ["ID", "TH", "SG"],
                "platform": "FAST",
                "force_data_mode": "clickhouse-mcp"
            }
            response = await client.post("/api/greenlight", json=payload)
            assert response.status_code == 502
            data = response.json()
            assert "detail" in data
            assert data["detail"]["error"] == "clickhouse_error"


@pytest.mark.asyncio
async def test_get_fleet_analytics_endpoint():
    """Verify fleet-wide OLAP analytics endpoint returns aggregated metrics."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        response = await client.get("/api/analytics/fleet?mode=fixture")
        assert response.status_code == 200
        data = response.json()
        assert data["total_titles"] == 12
        assert data["green_count"] == 5
        assert data["amber_count"] == 3
        assert data["red_count"] == 4
        assert data["fleet_readiness_pct"] > 0
        assert "ID" in data["territory_readiness"]
        assert "TH" in data["territory_readiness"]
        assert "SG" in data["territory_readiness"]
        assert len(data["bottleneck_distribution"]) > 0
        assert data["execution_time_ms"] >= 0


@pytest.mark.asyncio
async def test_remediate_master_video_loudness():
    """Verify agentic remediation generates FFmpeg loudness conformance work order."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-003",
            "territory": "ID",
            "category": "master_video",
            "reason": "Loudness -18.2 LUFS exceeds FAST standard (-24 LUFS)",
            "evidence": ["asset:ast-003-id-mv:ID:failed"],
            "owner": "Technical Operations",
            "next_action": "Remediate master QC failure",
        }
        response = await client.post("/api/remediate", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["action_type"] == "ffmpeg_loudness_conformance"
        assert "ffmpeg" in data["cli_command"]
        assert "loudnorm" in data["cli_command"]
        assert data["priority"] == "URGENT - LAUNCH BLOCKER"


@pytest.mark.asyncio
async def test_remediate_rights_expired():
    """Verify agentic remediation generates legal addendum memo for expired rights."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-001",
            "territory": "TH",
            "category": "rights",
            "reason": "Thailand FAST rights expired on 2026-06-30",
            "evidence": ["rights:slate-001:TH:contract-slate-001-th"],
            "owner": "Rights & Licensing",
            "next_action": "Renew FAST license",
        }
        response = await client.post("/api/remediate", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["action_type"] == "licensing_addendum_memo"
        assert "Rights" in data["assigned_team"]
        assert "ADDENDUM" in data["work_order_content"]


@pytest.mark.asyncio
async def test_remediate_subtitle_missing():
    """Verify agentic remediation generates vendor dispatch order for missing subtitle."""
    transport = ASGITransport(app=app)
    async with AsyncClient(transport=transport, base_url="http://test") as client:
        payload = {
            "title_id": "slate-004",
            "territory": "ID",
            "category": "subtitle",
            "reason": "Bahasa Indonesia subtitle missing in catalog",
            "evidence": ["asset:slate-004:ID:subtitle:missing"],
            "owner": "Localization",
            "next_action": "Deliver subtitle",
        }
        response = await client.post("/api/remediate", json=payload)
        assert response.status_code == 200
        data = response.json()
        assert data["action_type"] == "localization_dispatch_ticket"
        assert "subpqc" in (data["cli_command"] or "")

