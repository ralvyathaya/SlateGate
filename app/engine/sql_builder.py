"""
Safe Parameterized SQL Query Builder for ClickHouse Analytical Storage.
Enforces strictly read-only SELECT queries with input sanitization.
"""

import re
from datetime import date
from typing import List

# Whitelist patterns for SQL safety
TITLE_ID_PATTERN = re.compile(r"^[a-zA-Z0-9_\-]+$")
TERRITORY_PATTERN = re.compile(r"^[A-Z]{2}$")
PLATFORM_PATTERN = re.compile(r"^[A-Z0-9_\-]+$")

FORBIDDEN_SQL_KEYWORDS = [
    "INSERT", "UPDATE", "DELETE", "DROP", "ALTER", "TRUNCATE",
    "CREATE", "RENAME", "ATTACH", "DETACH", "OPTIMIZE", "KILL",
    "SYSTEM", "GRANT", "REVOKE"
]


def sanitize_string(val: str, pattern: re.Pattern, name: str) -> str:
    cleaned = str(val).strip()
    if not pattern.match(cleaned):
        raise ValueError(f"Invalid characters in {name}: '{val}'")
    return cleaned


def validate_query_safety(sql: str) -> None:
    """Ensure the SQL query contains only SELECT statements and no destructive commands."""
    normalized = sql.upper()
    
    # Must start with SELECT
    if not normalized.strip().startswith("SELECT"):
        raise ValueError("Security violation: Only SELECT queries are permitted.")
        
    for kw in FORBIDDEN_SQL_KEYWORDS:
        # Check for isolated keyword tokens
        if re.search(rf"\b{kw}\b", normalized):
            raise ValueError(f"Security violation: Forbidden keyword '{kw}' detected.")


def build_title_query(title_id: str, database: str = "slategate") -> str:
    """Builds safe query for title metadata."""
    safe_title_id = sanitize_string(title_id, TITLE_ID_PATTERN, "title_id")
    safe_db = sanitize_string(database, TITLE_ID_PATTERN, "database")
    
    sql = f"""
    SELECT
        title_id,
        title_name,
        original_language,
        genre,
        runtime_minutes,
        release_year,
        synopsis
    FROM {safe_db}.titles
    WHERE title_id = '{safe_title_id}'
    LIMIT 1
    """.strip()
    
    validate_query_safety(sql)
    return sql


def build_rights_query(
    title_id: str,
    launch_date: date,
    territories: List[str],
    platform: str,
    database: str = "slategate",
) -> str:
    """Builds safe query for territory rights windows."""
    safe_title_id = sanitize_string(title_id, TITLE_ID_PATTERN, "title_id")
    safe_platform = sanitize_string(platform.upper(), PLATFORM_PATTERN, "platform")
    safe_db = sanitize_string(database, TITLE_ID_PATTERN, "database")
    
    safe_territories = [
        f"'{sanitize_string(t.upper(), TERRITORY_PATTERN, 'territory')}'"
        for t in territories
    ]
    territories_in = ", ".join(safe_territories)
    date_str = launch_date.isoformat()

    sql = f"""
    SELECT
        rights_id,
        title_id,
        territory,
        platform,
        toString(start_date) AS start_date,
        toString(end_date) AS end_date,
        exclusive,
        contract_ref,
        has_conflict,
        conflict_notes
    FROM {safe_db}.rights_windows
    WHERE title_id = '{safe_title_id}'
      AND platform = '{safe_platform}'
      AND territory IN ({territories_in})
    ORDER BY territory, start_date
    """.strip()

    validate_query_safety(sql)
    return sql


def build_deliverables_query(
    platform: str,
    territories: List[str],
    database: str = "slategate",
) -> str:
    """Builds safe query for required deliverables specification."""
    safe_platform = sanitize_string(platform.upper(), PLATFORM_PATTERN, "platform")
    safe_db = sanitize_string(database, TITLE_ID_PATTERN, "database")
    
    safe_territories = [
        f"'{sanitize_string(t.upper(), TERRITORY_PATTERN, 'territory')}'"
        for t in territories
    ]
    territories_in = ", ".join(safe_territories)

    sql = f"""
    SELECT
        requirement_id,
        platform,
        territory,
        asset_type,
        is_mandatory,
        spec_details
    FROM {safe_db}.required_deliverables
    WHERE platform = '{safe_platform}'
      AND territory IN ({territories_in})
    ORDER BY territory, asset_type
    """.strip()

    validate_query_safety(sql)
    return sql


def build_assets_query(
    title_id: str,
    territories: List[str],
    database: str = "slategate",
) -> str:
    """Builds safe query for asset inventory and QC status."""
    safe_title_id = sanitize_string(title_id, TITLE_ID_PATTERN, "title_id")
    safe_db = sanitize_string(database, TITLE_ID_PATTERN, "database")
    
    safe_territories = [
        f"'{sanitize_string(t.upper(), TERRITORY_PATTERN, 'territory')}'"
        for t in territories
    ]
    territories_in = ", ".join(safe_territories)

    sql = f"""
    SELECT
        asset_id,
        title_id,
        territory,
        asset_type,
        file_path,
        qc_status,
        qc_notes,
        checksum
    FROM {safe_db}.assets
    WHERE title_id = '{safe_title_id}'
      AND territory IN ({territories_in})
    ORDER BY territory, asset_type
    """.strip()

    validate_query_safety(sql)
    return sql
