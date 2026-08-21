"""
Unit Tests for Deterministic Decision Policy Engine.
"""

from datetime import date
import pytest

from app.engine.fixtures import query_fixtures
from app.engine.policy import evaluate_greenlight
from app.models.response import DecisionEnum


def test_scenario_001_expired_thailand_rights_yields_red():
    """
    Scenario 1 (slate-001):
    - Thailand FAST rights expired on 2026-06-30 (target launch: 2026-09-15).
    - Indonesian subtitle missing; Thai artwork poster missing.
    - Expected Result: RED with rights evidence.
    """
    target_date = date(2026, 9, 15)
    territories = ["ID", "TH", "SG"]
    platform = "FAST"
    
    raw_data = query_fixtures("slate-001", territories, platform)
    tool_trace = ["fixture.query:rights_check", "fixture.query:readiness_check"]
    
    response = evaluate_greenlight(
        title_id="slate-001",
        launch_date=target_date,
        territories=territories,
        platform=platform,
        raw_data=raw_data,
        tool_trace=tool_trace,
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.RED
    assert response.passed_count > 0
    assert response.failed_count > 0
    assert "rights" in response.summary.lower() or "blocked" in response.summary.lower()

    # Check evidence for expired TH rights
    th_rights_check = next(
        (c for c in response.checks if c.category == "rights" and c.territory == "TH"),
        None
    )
    assert th_rights_check is not None
    assert th_rights_check.status == "fail"
    assert "contract-slate-001-th" in str(th_rights_check.evidence)
    assert th_rights_check.owner == "Rights & Licensing"


def test_scenario_002_fully_ready_yields_green():
    """
    Scenario 2 (slate-002):
    - Valid rights across ID, TH, SG through 2028.
    - Master video passed QC.
    - Subtitles, artwork, metadata passed QC.
    - Expected Result: GREEN.
    """
    target_date = date(2026, 9, 15)
    territories = ["ID", "TH", "SG"]
    platform = "FAST"
    
    raw_data = query_fixtures("slate-002", territories, platform)
    tool_trace = ["fixture.query:rights_check", "fixture.query:readiness_check"]
    
    response = evaluate_greenlight(
        title_id="slate-002",
        launch_date=target_date,
        territories=territories,
        platform=platform,
        raw_data=raw_data,
        tool_trace=tool_trace,
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.GREEN
    assert response.failed_count == 0
    assert response.passed_count == response.total_count
    assert response.total_count > 0
    assert "APPROVED" in response.summary.upper()
    
    # All checks must have evidence
    for check in response.checks:
        assert check.status == "pass"
        assert len(check.evidence) > 0


def test_scenario_003_master_video_qc_fail_yields_red():
    """
    Scenario 3 (slate-003):
    - Valid rights across ID, TH, SG.
    - ID Master video failed QC (loudness out of spec).
    - Expected Result: RED.
    """
    target_date = date(2026, 9, 15)
    territories = ["ID", "TH", "SG"]
    platform = "FAST"
    
    raw_data = query_fixtures("slate-003", territories, platform)
    tool_trace = ["fixture.query:rights_check", "fixture.query:readiness_check"]
    
    response = evaluate_greenlight(
        title_id="slate-003",
        launch_date=target_date,
        territories=territories,
        platform=platform,
        raw_data=raw_data,
        tool_trace=tool_trace,
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.RED
    id_master_check = next(
        (c for c in response.checks if c.category == "master_video" and c.territory == "ID"),
        None
    )
    assert id_master_check is not None
    assert id_master_check.status == "fail"
    assert id_master_check.owner == "Technical Operations"
    assert "failed" in id_master_check.reason.lower()


def test_scenario_004_missing_subtitle_yields_amber():
    """
    Scenario 4 (slate-004):
    - Valid rights and master video.
    - Indonesian subtitle track missing.
    - Expected Result: AMBER.
    """
    target_date = date(2026, 9, 15)
    territories = ["ID", "TH", "SG"]
    platform = "FAST"
    
    raw_data = query_fixtures("slate-004", territories, platform)
    tool_trace = ["fixture.query:rights_check", "fixture.query:readiness_check"]
    
    response = evaluate_greenlight(
        title_id="slate-004",
        launch_date=target_date,
        territories=territories,
        platform=platform,
        raw_data=raw_data,
        tool_trace=tool_trace,
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.AMBER
    
    id_sub_check = next(
        (c for c in response.checks if c.category == "subtitle" and c.territory == "ID"),
        None
    )
    assert id_sub_check is not None
    assert id_sub_check.status == "fail"
    assert id_sub_check.owner == "Localization"


def test_missing_title_in_catalog_never_green():
    """
    When title does not exist in catalog, must return RED, never GREEN.
    """
    response = evaluate_greenlight(
        title_id="slate-nonexistent",
        launch_date=date(2026, 9, 15),
        territories=["ID", "TH"],
        platform="FAST",
        raw_data={"title": None, "rights": [], "deliverables": [], "assets": []},
        tool_trace=["fixture.query:title_metadata"],
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.RED
    assert response.failed_count > 0
    assert response.passed_count == 0


def test_empty_database_rows_never_green():
    """
    When rights or assets data is empty, must fail safely with RED/AMBER, never GREEN.
    """
    raw_data = {
        "title": {"title_id": "slate-test", "title_name": "Test Title"},
        "rights": [], # No rights
        "deliverables": [],
        "assets": [], # No assets
    }
    
    response = evaluate_greenlight(
        title_id="slate-test",
        launch_date=date(2026, 9, 15),
        territories=["ID", "TH", "SG"],
        platform="FAST",
        raw_data=raw_data,
        tool_trace=["fixture.query:test"],
        data_mode="fixture",
    )
    
    assert response.decision == DecisionEnum.RED
    assert response.failed_count > 0
