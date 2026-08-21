-- ============================================================================
-- SlateGate — ClickHouse DDL Schema
-- Content Greenlight Analytical Storage Layer
-- ============================================================================

CREATE DATABASE IF NOT EXISTS slategate;

-- 1. Titles Catalog Table
CREATE TABLE IF NOT EXISTS slategate.titles
(
    title_id String,
    title_name String,
    original_language LowCardinality(String),
    genre LowCardinality(String),
    runtime_minutes UInt32,
    release_year UInt16,
    synopsis String,
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PRIMARY KEY (title_id)
ORDER BY (title_id);

-- 2. Territory & Platform Rights Windows
CREATE TABLE IF NOT EXISTS slategate.rights_windows
(
    rights_id String,
    title_id String,
    territory LowCardinality(String),
    platform LowCardinality(String),
    start_date Date,
    end_date Date,
    exclusive UInt8,
    contract_ref String,
    has_conflict UInt8,
    conflict_notes String,
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PRIMARY KEY (title_id, territory, platform, rights_id)
ORDER BY (title_id, territory, platform, start_date, rights_id);

-- 3. Required Deliverable Specifications per Platform & Territory
CREATE TABLE IF NOT EXISTS slategate.required_deliverables
(
    requirement_id String,
    platform LowCardinality(String),
    territory LowCardinality(String),
    asset_type LowCardinality(String),
    is_mandatory UInt8,
    spec_details String,
    created_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PRIMARY KEY (platform, territory, asset_type, requirement_id)
ORDER BY (platform, territory, asset_type, requirement_id);

-- 4. Ingested Asset Inventory & QC Register
CREATE TABLE IF NOT EXISTS slategate.assets
(
    asset_id String,
    title_id String,
    territory LowCardinality(String),
    asset_type LowCardinality(String),
    file_path String,
    qc_status LowCardinality(String),
    qc_notes String,
    checksum String,
    updated_at DateTime DEFAULT now()
)
ENGINE = MergeTree()
PRIMARY KEY (title_id, territory, asset_type, asset_id)
ORDER BY (title_id, territory, asset_type, asset_id);
