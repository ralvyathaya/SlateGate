"""
Tests for ClickHouse MCP Runtime Integration and Tool Provenance.
"""

from datetime import date
from unittest.mock import AsyncMock, patch
import pytest

from app.agent.launch_director import LaunchDirectorAgent
from app.mcp.client import ClickHouseMcpClient
from app.models.request import GreenlightRequest


@pytest.mark.asyncio
async def test_fixture_trace_does_not_claim_mcp_partner():
    """
    Ensure fixture executions record 'fixture.query:*' and NEVER claim 'mcp-clickhouse.run_query'.
    """
    client = ClickHouseMcpClient()
    raw_data, tool_trace, data_mode = await client.fetch_greenlight_data(
        title_id="slate-001",
        launch_date=date(2026, 9, 15),
        territories=["ID", "TH", "SG"],
        platform="FAST",
        force_data_mode="fixture",
    )
    
    assert data_mode == "fixture"
    for trace in tool_trace:
        assert "fixture.query" in trace
        assert "mcp-clickhouse" not in trace


@pytest.mark.asyncio
async def test_live_mcp_trace_includes_mcp_run_query():
    """
    Ensure live MCP executions accurately record 'mcp-clickhouse.run_query:*'.
    """
    client = ClickHouseMcpClient()
    # Mock the actual execution method to return valid data structure
    mock_rows = [{"title_id": "slate-002", "title_name": "Singa City Beats"}]
    
    with patch.object(client, "run_mcp_stdio_query", new_callable=AsyncMock) as mock_run:
        mock_run.return_value = mock_rows
        
        raw_data, tool_trace, data_mode = await client.fetch_greenlight_data(
            title_id="slate-002",
            launch_date=date(2026, 9, 15),
            territories=["ID", "TH", "SG"],
            platform="FAST",
            force_data_mode="clickhouse-mcp",
        )
        
        assert data_mode == "clickhouse-mcp"
        assert any("mcp-clickhouse.run_query:rights_check" in t for t in tool_trace)
        assert any("mcp-clickhouse.run_query:readiness_check" in t for t in tool_trace)


@pytest.mark.asyncio
async def test_launch_director_agent_trace():
    """
    Verify LaunchDirectorAgent includes agent step in tool_trace.
    """
    agent = LaunchDirectorAgent()
    req = GreenlightRequest(
        title_id="slate-002",
        launch_date=date(2026, 9, 15),
        territories=["ID", "TH", "SG"],
        platform="FAST",
        force_data_mode="fixture",
    )
    response = await agent.execute_audit(req)
    assert any("launch_director" in t for t in response.tool_trace)
