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
