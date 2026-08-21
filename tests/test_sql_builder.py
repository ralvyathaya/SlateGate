"""
Security and Safety Tests for ClickHouse SQL Query Builder.
"""

from datetime import date
import pytest

from app.engine.sql_builder import (
    build_assets_query,
    build_deliverables_query,
    build_rights_query,
    build_title_query,
    validate_query_safety,
)


def test_safe_sql_generation():
    """Verify clean parameterized SELECT query generation."""
    sql = build_rights_query(
        title_id="slate-001",
        launch_date=date(2026, 9, 15),
        territories=["ID", "TH", "SG"],
        platform="FAST",
        database="slategate",
    )
    assert "SELECT" in sql
    assert "slategate.rights_windows" in sql
    assert "'ID', 'TH', 'SG'" in sql
    assert "'slate-001'" in sql


def test_blocks_destructive_keywords():
    """Verify that forbidden SQL operations raise ValueError."""
    dangerous_queries = [
        "DROP TABLE slategate.titles",
        "TRUNCATE TABLE slategate.assets",
        "DELETE FROM slategate.rights_windows WHERE 1=1",
        "ALTER TABLE slategate.assets DROP COLUMN file_path",
        "INSERT INTO slategate.titles VALUES ('x')",
        "UPDATE slategate.assets SET qc_status = 'passed'",
    ]
    for q in dangerous_queries:
        with pytest.raises(ValueError, match="Security violation"):
            validate_query_safety(q)


def test_rejects_sql_injection_in_title_id():
    """Verify SQL injection in title_id is rejected by whitelist validator."""
    bad_title = "slate-001'; DROP TABLE titles; --"
    with pytest.raises(ValueError, match="Invalid characters in title_id"):
        build_title_query(bad_title)


def test_rejects_invalid_territory_code():
    """Verify non-ISO territory code is rejected."""
    bad_territories = ["ID", "MALICIOUS_INPUT"]
    with pytest.raises(ValueError, match="Invalid characters in territory"):
        build_deliverables_query(platform="FAST", territories=bad_territories)
