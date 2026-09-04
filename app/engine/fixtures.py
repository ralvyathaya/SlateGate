"""
Synthetic Test and Demo Fixtures for SlateGate.
Mirrors the ClickHouse seed data for local testing and zero-dependency offline demos.
"""

from typing import Any, Dict, List

TITLES_FIXTURE: List[Dict[str, Any]] = [
    {
        "title_id": "slate-001",
        "title_name": "The Nusantara Heist",
        "original_language": "id",
        "genre": "Action / Heist",
        "runtime_minutes": 114,
        "release_year": 2025,
        "synopsis": "A daring crew of elite hackers and operatives plan a high-stakes museum heist across Jakarta, Bangkok, and Singapore.",
    },
    {
        "title_id": "slate-002",
        "title_name": "Singa City Beats",
        "original_language": "en",
        "genre": "Music / Drama",
        "runtime_minutes": 98,
        "release_year": 2026,
        "synopsis": "An underground electronic music producer in Singapore navigates cross-border festivals in Southeast Asia while overcoming family expectations.",
    },
    {
        "title_id": "slate-003",
        "title_name": "Bangkok Neon Nights",
        "original_language": "th",
        "genre": "Neo-Noir / Crime",
        "runtime_minutes": 105,
        "release_year": 2025,
        "synopsis": "A detective uncovers a syndicate controlling deepwater trade channels along the Chao Phraya river under the city neon glow.",
    },
    {
        "title_id": "slate-004",
        "title_name": "Java Horizon",
        "original_language": "id",
        "genre": "Adventure / Romance",
        "runtime_minutes": 122,
        "release_year": 2026,
        "synopsis": "Two documentary filmmakers traverse the volcanic ridges of East Java in search of an ancient spice route legend.",
    },
    {
        "title_id": "slate-005",
        "title_name": "Borneo Shadows",
        "original_language": "id",
        "genre": "Horror / Supernatural",
        "runtime_minutes": 102,
        "release_year": 2025,
        "synopsis": "A team of researchers exploring deep rainforest canopies in Kalimantan awakens a mythological ancestral guardian.",
    },
    {
        "title_id": "slate-006",
        "title_name": "Chiang Mai Express",
        "original_language": "th",
        "genre": "Comedy / Road Trip",
        "runtime_minutes": 110,
        "release_year": 2026,
        "synopsis": "Three estranged cousins embark on an unpredictable sleeper train journey from Bangkok to Chiang Mai with a priceless heirloom.",
    },
    {
        "title_id": "slate-007",
        "title_name": "Marina Bay Confidential",
        "original_language": "en",
        "genre": "Thriller / Mystery",
        "runtime_minutes": 118,
        "release_year": 2025,
        "synopsis": "A cyber intelligence officer investigates an international corporate espionage ring operating out of Singapore fintech hubs.",
    },
    {
        "title_id": "slate-008",
        "title_name": "Krakatoa: The Fire Within",
        "original_language": "id",
        "genre": "Documentary",
        "runtime_minutes": 89,
        "release_year": 2026,
        "synopsis": "Stunning 4K documentation of volcanologists capturing never-before-seen geological phenomena in the Sunda Strait.",
    },
    {
        "title_id": "slate-009",
        "title_name": "Batik Warriors",
        "original_language": "id",
        "genre": "Animation / Action",
        "runtime_minutes": 95,
        "release_year": 2026,
        "synopsis": "An epic animated fantasy weaving traditional Indonesian textile folklore into a futuristic heroic martial arts saga.",
    },
    {
        "title_id": "slate-010",
        "title_name": "Phuket Blue",
        "original_language": "th",
        "genre": "Romance / Drama",
        "runtime_minutes": 108,
        "release_year": 2025,
        "synopsis": "Two marine biologists find unexpected romance while restoring coral reefs along the Andaman Sea coastline.",
    },
    {
        "title_id": "slate-011",
        "title_name": "Jakarta Underground",
        "original_language": "id",
        "genre": "Crime / Drama",
        "runtime_minutes": 115,
        "release_year": 2026,
        "synopsis": "A fearless investigative journalist unravels criminal syndicates entrenched inside the megacity public transit expansion.",
    },
    {
        "title_id": "slate-012",
        "title_name": "Echoes of Malacca",
        "original_language": "en",
        "genre": "Historical / Drama",
        "runtime_minutes": 130,
        "release_year": 2025,
        "synopsis": "A sweeping multi-generational chronicle tracing merchants and maritime navigators through 500 years of the Malacca Strait.",
    },
]

REQUIRED_DELIVERABLES_FIXTURE: List[Dict[str, Any]] = [
    # ID FAST Deliverables
    {"requirement_id": "req-fast-id-master", "platform": "FAST", "territory": "ID", "asset_type": "master_video", "is_mandatory": 1, "spec_details": "ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)"},
    {"requirement_id": "req-fast-id-sub", "platform": "FAST", "territory": "ID", "asset_type": "subtitle", "is_mandatory": 1, "spec_details": "Bahasa Indonesia localized SRT/VTT (UTF-8)"},
    {"requirement_id": "req-fast-id-poster", "platform": "FAST", "territory": "ID", "asset_type": "artwork_poster", "is_mandatory": 1, "spec_details": "2:3 Portrait Key Art 2000x3000 JPG/PNG with localized title treatment"},
    {"requirement_id": "req-fast-id-banner", "platform": "FAST", "territory": "ID", "asset_type": "artwork_banner", "is_mandatory": 1, "spec_details": "16:9 Landscape Hero Banner 3840x2160 JPG"},
    {"requirement_id": "req-fast-id-meta", "platform": "FAST", "territory": "ID", "asset_type": "metadata", "is_mandatory": 1, "spec_details": "Localized Indonesian title, synopsis, cast, content rating"},

    # TH FAST Deliverables
    {"requirement_id": "req-fast-th-master", "platform": "FAST", "territory": "TH", "asset_type": "master_video", "is_mandatory": 1, "spec_details": "ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)"},
    {"requirement_id": "req-fast-th-sub", "platform": "FAST", "territory": "TH", "asset_type": "subtitle", "is_mandatory": 1, "spec_details": "Thai localized SRT/VTT (UTF-8)"},
    {"requirement_id": "req-fast-th-poster", "platform": "FAST", "territory": "TH", "asset_type": "artwork_poster", "is_mandatory": 1, "spec_details": "2:3 Portrait Key Art 2000x3000 JPG/PNG with localized title treatment"},
    {"requirement_id": "req-fast-th-banner", "platform": "FAST", "territory": "TH", "asset_type": "artwork_banner", "is_mandatory": 1, "spec_details": "16:9 Landscape Hero Banner 3840x2160 JPG"},
    {"requirement_id": "req-fast-th-meta", "platform": "FAST", "territory": "TH", "asset_type": "metadata", "is_mandatory": 1, "spec_details": "Localized Thai title, synopsis, cast, content rating"},

    # SG FAST Deliverables
    {"requirement_id": "req-fast-sg-master", "platform": "FAST", "territory": "SG", "asset_type": "master_video", "is_mandatory": 1, "spec_details": "ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)"},
    {"requirement_id": "req-fast-sg-sub", "platform": "FAST", "territory": "SG", "asset_type": "subtitle", "is_mandatory": 1, "spec_details": "English / Simplified Chinese SRT/VTT (UTF-8)"},
    {"requirement_id": "req-fast-sg-poster", "platform": "FAST", "territory": "SG", "asset_type": "artwork_poster", "is_mandatory": 1, "spec_details": "2:3 Portrait Key Art 2000x3000 JPG/PNG with bilingual title treatment"},
    {"requirement_id": "req-fast-sg-banner", "platform": "FAST", "territory": "SG", "asset_type": "artwork_banner", "is_mandatory": 1, "spec_details": "16:9 Landscape Hero Banner 3840x2160 JPG"},
    {"requirement_id": "req-fast-sg-meta", "platform": "FAST", "territory": "SG", "asset_type": "metadata", "is_mandatory": 1, "spec_details": "Localized English / Chinese title, synopsis, IMDA rating"},
]

RIGHTS_WINDOWS_FIXTURE: List[Dict[str, Any]] = [
    # slate-001: TH rights EXPIRED on 2026-06-30
    {"rights_id": "rw-001-id", "title_id": "slate-001", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2027-12-31", "exclusive": 1, "contract_ref": "contract-slate-001-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-001-th", "title_id": "slate-001", "territory": "TH", "platform": "FAST", "start_date": "2025-01-01", "end_date": "2026-06-30", "exclusive": 1, "contract_ref": "contract-slate-001-th", "has_conflict": 0, "conflict_notes": "Window lapsed without option exercise"},
    {"rights_id": "rw-001-sg", "title_id": "slate-001", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2027-12-31", "exclusive": 1, "contract_ref": "contract-slate-001-sg", "has_conflict": 0, "conflict_notes": ""},

    # slate-002: Fully valid
    {"rights_id": "rw-002-id", "title_id": "slate-002", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-002-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-002-th", "title_id": "slate-002", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-002-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-002-sg", "title_id": "slate-002", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-002-sg", "has_conflict": 0, "conflict_notes": ""},

    # slate-003: Fully valid
    {"rights_id": "rw-003-id", "title_id": "slate-003", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2027-12-31", "exclusive": 1, "contract_ref": "contract-slate-003-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-003-th", "title_id": "slate-003", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2027-12-31", "exclusive": 1, "contract_ref": "contract-slate-003-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-003-sg", "title_id": "slate-003", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2027-12-31", "exclusive": 1, "contract_ref": "contract-slate-003-sg", "has_conflict": 0, "conflict_notes": ""},

    # slate-004: Fully valid
    {"rights_id": "rw-004-id", "title_id": "slate-004", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-004-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-004-th", "title_id": "slate-004", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-004-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-004-sg", "title_id": "slate-004", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-004-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-005-id", "title_id": "slate-005", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-005-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-005-th", "title_id": "slate-005", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-005-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-005-sg", "title_id": "slate-005", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-005-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-006-id", "title_id": "slate-006", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-006-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-006-th", "title_id": "slate-006", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-006-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-006-sg", "title_id": "slate-006", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-006-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-007-id", "title_id": "slate-007", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-007-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-007-th", "title_id": "slate-007", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-007-th", "has_conflict": 1, "conflict_notes": "Conflict with Thai linear broadcast exclusivity window"},
    {"rights_id": "rw-007-sg", "title_id": "slate-007", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-007-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-008-id", "title_id": "slate-008", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-008-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-008-th", "title_id": "slate-008", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-008-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-008-sg", "title_id": "slate-008", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-008-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-009-id", "title_id": "slate-009", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-009-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-009-th", "title_id": "slate-009", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-009-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-009-sg", "title_id": "slate-009", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-009-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-010-id", "title_id": "slate-010", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-010-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-010-th", "title_id": "slate-010", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-010-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-010-sg", "title_id": "slate-010", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-010-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-011-id", "title_id": "slate-011", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-011-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-011-th", "title_id": "slate-011", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-011-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-011-sg", "title_id": "slate-011", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-011-sg", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-012-id", "title_id": "slate-012", "territory": "ID", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-012-id", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-012-th", "title_id": "slate-012", "territory": "TH", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-012-th", "has_conflict": 0, "conflict_notes": ""},
    {"rights_id": "rw-012-sg", "title_id": "slate-012", "territory": "SG", "platform": "FAST", "start_date": "2026-01-01", "end_date": "2028-12-31", "exclusive": 1, "contract_ref": "contract-slate-012-sg", "has_conflict": 0, "conflict_notes": ""},
]

ASSETS_FIXTURE: List[Dict[str, Any]] = [
    # slate-001
    {"asset_id": "ast-001-id-mv", "title_id": "slate-001", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-001/id/master_1080p.mov", "qc_status": "passed", "qc_notes": "QC clean, ProRes 422 HQ, -23.8 LUFS", "checksum": "sha256:7f9a01"},
    {"asset_id": "ast-001-id-art-b", "title_id": "slate-001", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-001/id/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Resolution 3840x2160 confirmed", "checksum": "sha256:7f9a02"},
    {"asset_id": "ast-001-id-art-p", "title_id": "slate-001", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-001/id/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Resolution 2000x3000 confirmed", "checksum": "sha256:7f9a03"},
    {"asset_id": "ast-001-id-meta", "title_id": "slate-001", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-001/id/metadata.json", "qc_status": "passed", "qc_notes": "Title, synopsis, age rating valid", "checksum": "sha256:7f9a04"},
    # ID subtitle missing in slate-001

    {"asset_id": "ast-001-th-mv", "title_id": "slate-001", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-001/th/master_1080p.mov", "qc_status": "passed", "qc_notes": "QC clean, ProRes 422 HQ", "checksum": "sha256:7f9a05"},
    {"asset_id": "ast-001-th-sub", "title_id": "slate-001", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-001/th/subtitles_th.srt", "qc_status": "passed", "qc_notes": "Thai timing verified", "checksum": "sha256:7f9a06"},
    {"asset_id": "ast-001-th-art-b", "title_id": "slate-001", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-001/th/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Resolution 3840x2160 confirmed", "checksum": "sha256:7f9a07"},
    {"asset_id": "ast-001-th-meta", "title_id": "slate-001", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-001/th/metadata.json", "qc_status": "passed", "qc_notes": "Thai metadata verified", "checksum": "sha256:7f9a08"},
    # TH artwork_poster missing in slate-001

    {"asset_id": "ast-001-sg-mv", "title_id": "slate-001", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-001/sg/master_1080p.mov", "qc_status": "passed", "qc_notes": "QC clean, ProRes 422 HQ", "checksum": "sha256:7f9a09"},
    {"asset_id": "ast-001-sg-sub", "title_id": "slate-001", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-001/sg/subtitles_en.srt", "qc_status": "passed", "qc_notes": "English subtitles verified", "checksum": "sha256:7f9a10"},
    {"asset_id": "ast-001-sg-art-p", "title_id": "slate-001", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-001/sg/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:7f9a11"},
    {"asset_id": "ast-001-sg-art-b", "title_id": "slate-001", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-001/sg/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:7f9a12"},
    {"asset_id": "ast-001-sg-meta", "title_id": "slate-001", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-001/sg/metadata.json", "qc_status": "passed", "qc_notes": "IMDA PG13 metadata verified", "checksum": "sha256:7f9a13"},

    # slate-002: ALL passed in ID, TH, SG
    {"asset_id": "ast-002-id-mv", "title_id": "slate-002", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-002/id/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.1 LUFS broadcast ready", "checksum": "sha256:8b0101"},
    {"asset_id": "ast-002-id-sub", "title_id": "slate-002", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-002/id/subtitles_id.srt", "qc_status": "passed", "qc_notes": "Bahasa Indonesia UTF-8 certified", "checksum": "sha256:8b0102"},
    {"asset_id": "ast-002-id-art-p", "title_id": "slate-002", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-002/id/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "2000x3000 verified", "checksum": "sha256:8b0103"},
    {"asset_id": "ast-002-id-art-b", "title_id": "slate-002", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-002/id/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "3840x2160 verified", "checksum": "sha256:8b0104"},
    {"asset_id": "ast-002-id-meta", "title_id": "slate-002", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-002/id/metadata.json", "qc_status": "passed", "qc_notes": "Complete ID metadata", "checksum": "sha256:8b0105"},

    {"asset_id": "ast-002-th-mv", "title_id": "slate-002", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-002/th/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -23.9 LUFS", "checksum": "sha256:8b0106"},
    {"asset_id": "ast-002-th-sub", "title_id": "slate-002", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-002/th/subtitles_th.srt", "qc_status": "passed", "qc_notes": "Thai UTF-8 certified", "checksum": "sha256:8b0107"},
    {"asset_id": "ast-002-th-art-p", "title_id": "slate-002", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-002/th/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "2000x3000 verified", "checksum": "sha256:8b0108"},
    {"asset_id": "ast-002-th-art-b", "title_id": "slate-002", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-002/th/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "3840x2160 verified", "checksum": "sha256:8b0109"},
    {"asset_id": "ast-002-th-meta", "title_id": "slate-002", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-002/th/metadata.json", "qc_status": "passed", "qc_notes": "Complete TH metadata", "checksum": "sha256:8b0110"},

    {"asset_id": "ast-002-sg-mv", "title_id": "slate-002", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-002/sg/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:8b0111"},
    {"asset_id": "ast-002-sg-sub", "title_id": "slate-002", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-002/sg/subtitles_en.srt", "qc_status": "passed", "qc_notes": "English/Chinese UTF-8 certified", "checksum": "sha256:8b0112"},
    {"asset_id": "ast-002-sg-art-p", "title_id": "slate-002", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-002/sg/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "2000x3000 verified", "checksum": "sha256:8b0113"},
    {"asset_id": "ast-002-sg-art-b", "title_id": "slate-002", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-002/sg/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "3840x2160 verified", "checksum": "sha256:8b0114"},
    {"asset_id": "ast-002-sg-meta", "title_id": "slate-002", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-002/sg/metadata.json", "qc_status": "passed", "qc_notes": "Complete SG IMDA metadata", "checksum": "sha256:8b0115"},

    # slate-003: ID master video FAILED QC
    {"asset_id": "ast-003-id-mv", "title_id": "slate-003", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-003/id/master_1080p.mov", "qc_status": "failed", "qc_notes": "Loudness failed: -18.2 LUFS exceeds FAST standard (-24.0 +/- 1 LUFS). Audio clipping detected at 00:42:15.", "checksum": "sha256:9c0201"},
    {"asset_id": "ast-003-id-sub", "title_id": "slate-003", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-003/id/subtitles_id.srt", "qc_status": "passed", "qc_notes": "Bahasa Indonesia subtitles verified", "checksum": "sha256:9c0202"},
    {"asset_id": "ast-003-id-art-p", "title_id": "slate-003", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-003/id/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:9c0203"},
    {"asset_id": "ast-003-id-art-b", "title_id": "slate-003", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-003/id/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:9c0204"},
    {"asset_id": "ast-003-id-meta", "title_id": "slate-003", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-003/id/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:9c0205"},

    {"asset_id": "ast-003-th-mv", "title_id": "slate-003", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-003/th/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:9c0206"},
    {"asset_id": "ast-003-th-sub", "title_id": "slate-003", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-003/th/subtitles_th.srt", "qc_status": "passed", "qc_notes": "Thai subtitles verified", "checksum": "sha256:9c0207"},
    {"asset_id": "ast-003-th-art-p", "title_id": "slate-003", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-003/th/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:9c0208"},
    {"asset_id": "ast-003-th-art-b", "title_id": "slate-003", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-003/th/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:9c0209"},
    {"asset_id": "ast-003-th-meta", "title_id": "slate-003", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-003/th/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:9c0210"},

    {"asset_id": "ast-003-sg-mv", "title_id": "slate-003", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-003/sg/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:9c0211"},
    {"asset_id": "ast-003-sg-sub", "title_id": "slate-003", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-003/sg/subtitles_en.srt", "qc_status": "passed", "qc_notes": "English subtitles verified", "checksum": "sha256:9c0212"},
    {"asset_id": "ast-003-sg-art-p", "title_id": "slate-003", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-003/sg/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:9c0213"},
    {"asset_id": "ast-003-sg-art-b", "title_id": "slate-003", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-003/sg/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:9c0214"},
    {"asset_id": "ast-003-sg-meta", "title_id": "slate-003", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-003/sg/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:9c0215"},

    # slate-004: ID subtitle MISSING
    {"asset_id": "ast-004-id-mv", "title_id": "slate-004", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-004/id/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:ad0301"},
    # ID subtitle missing in slate-004
    {"asset_id": "ast-004-id-art-p", "title_id": "slate-004", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-004/id/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:ad0302"},
    {"asset_id": "ast-004-id-art-b", "title_id": "slate-004", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-004/id/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:ad0303"},
    {"asset_id": "ast-004-id-meta", "title_id": "slate-004", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-004/id/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:ad0304"},

    {"asset_id": "ast-004-th-mv", "title_id": "slate-004", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-004/th/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:ad0305"},
    {"asset_id": "ast-004-th-sub", "title_id": "slate-004", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-004/th/subtitles_th.srt", "qc_status": "passed", "qc_notes": "Thai subtitles verified", "checksum": "sha256:ad0306"},
    {"asset_id": "ast-004-th-art-p", "title_id": "slate-004", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-004/th/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:ad0307"},
    {"asset_id": "ast-004-th-art-b", "title_id": "slate-004", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-004/th/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:ad0308"},
    {"asset_id": "ast-004-th-meta", "title_id": "slate-004", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-004/th/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:ad0309"},

    {"asset_id": "ast-004-sg-mv", "title_id": "slate-004", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-004/sg/master_1080p.mov", "qc_status": "passed", "qc_notes": "ProRes 422 HQ, -24.0 LUFS", "checksum": "sha256:ad0310"},
    {"asset_id": "ast-004-sg-sub", "title_id": "slate-004", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-004/sg/subtitles_en.srt", "qc_status": "passed", "qc_notes": "English subtitles verified", "checksum": "sha256:ad0311"},
    {"asset_id": "ast-004-sg-art-p", "title_id": "slate-004", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-004/sg/poster_2x3.jpg", "qc_status": "passed", "qc_notes": "Poster verified", "checksum": "sha256:ad0312"},
    {"asset_id": "ast-004-sg-art-b", "title_id": "slate-004", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-004/sg/hero_banner_16x9.jpg", "qc_status": "passed", "qc_notes": "Banner verified", "checksum": "sha256:ad0313"},
    {"asset_id": "ast-004-sg-meta", "title_id": "slate-004", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-004/sg/metadata.json", "qc_status": "passed", "qc_notes": "Metadata verified", "checksum": "sha256:ad0314"},
    {"asset_id": "ast-005-id-master_video", "title_id": "slate-005", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-005/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05id"},
    {"asset_id": "ast-005-id-subtitle", "title_id": "slate-005", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-005/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05id"},
    {"asset_id": "ast-005-id-artwork_poster", "title_id": "slate-005", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-005/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05id"},
    {"asset_id": "ast-005-id-artwork_banner", "title_id": "slate-005", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-005/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05id"},
    {"asset_id": "ast-005-id-metadata", "title_id": "slate-005", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-005/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05id"},
    {"asset_id": "ast-005-th-master_video", "title_id": "slate-005", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-005/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05th"},
    {"asset_id": "ast-005-th-subtitle", "title_id": "slate-005", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-005/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05th"},
    {"asset_id": "ast-005-th-artwork_poster", "title_id": "slate-005", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-005/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05th"},
    {"asset_id": "ast-005-th-artwork_banner", "title_id": "slate-005", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-005/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05th"},
    {"asset_id": "ast-005-th-metadata", "title_id": "slate-005", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-005/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05th"},
    {"asset_id": "ast-005-sg-master_video", "title_id": "slate-005", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-005/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05sg"},
    {"asset_id": "ast-005-sg-subtitle", "title_id": "slate-005", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-005/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05sg"},
    {"asset_id": "ast-005-sg-artwork_poster", "title_id": "slate-005", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-005/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05sg"},
    {"asset_id": "ast-005-sg-artwork_banner", "title_id": "slate-005", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-005/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05sg"},
    {"asset_id": "ast-005-sg-metadata", "title_id": "slate-005", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-005/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b05sg"},
    {"asset_id": "ast-006-id-master_video", "title_id": "slate-006", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-006/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06id"},
    {"asset_id": "ast-006-id-artwork_poster", "title_id": "slate-006", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-006/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06id"},
    {"asset_id": "ast-006-id-artwork_banner", "title_id": "slate-006", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-006/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06id"},
    {"asset_id": "ast-006-id-metadata", "title_id": "slate-006", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-006/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06id"},
    {"asset_id": "ast-006-th-master_video", "title_id": "slate-006", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-006/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06th"},
    {"asset_id": "ast-006-th-subtitle", "title_id": "slate-006", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-006/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06th"},
    {"asset_id": "ast-006-th-artwork_poster", "title_id": "slate-006", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-006/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06th"},
    {"asset_id": "ast-006-th-artwork_banner", "title_id": "slate-006", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-006/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06th"},
    {"asset_id": "ast-006-th-metadata", "title_id": "slate-006", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-006/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06th"},
    {"asset_id": "ast-006-sg-master_video", "title_id": "slate-006", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-006/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06sg"},
    {"asset_id": "ast-006-sg-subtitle", "title_id": "slate-006", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-006/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06sg"},
    {"asset_id": "ast-006-sg-artwork_poster", "title_id": "slate-006", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-006/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06sg"},
    {"asset_id": "ast-006-sg-artwork_banner", "title_id": "slate-006", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-006/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06sg"},
    {"asset_id": "ast-006-sg-metadata", "title_id": "slate-006", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-006/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b06sg"},
    {"asset_id": "ast-007-id-master_video", "title_id": "slate-007", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-007/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07id"},
    {"asset_id": "ast-007-id-subtitle", "title_id": "slate-007", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-007/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07id"},
    {"asset_id": "ast-007-id-artwork_poster", "title_id": "slate-007", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-007/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07id"},
    {"asset_id": "ast-007-id-artwork_banner", "title_id": "slate-007", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-007/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07id"},
    {"asset_id": "ast-007-id-metadata", "title_id": "slate-007", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-007/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07id"},
    {"asset_id": "ast-007-th-master_video", "title_id": "slate-007", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-007/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07th"},
    {"asset_id": "ast-007-th-subtitle", "title_id": "slate-007", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-007/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07th"},
    {"asset_id": "ast-007-th-artwork_poster", "title_id": "slate-007", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-007/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07th"},
    {"asset_id": "ast-007-th-artwork_banner", "title_id": "slate-007", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-007/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07th"},
    {"asset_id": "ast-007-th-metadata", "title_id": "slate-007", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-007/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07th"},
    {"asset_id": "ast-007-sg-master_video", "title_id": "slate-007", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-007/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07sg"},
    {"asset_id": "ast-007-sg-subtitle", "title_id": "slate-007", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-007/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07sg"},
    {"asset_id": "ast-007-sg-artwork_poster", "title_id": "slate-007", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-007/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07sg"},
    {"asset_id": "ast-007-sg-artwork_banner", "title_id": "slate-007", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-007/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07sg"},
    {"asset_id": "ast-007-sg-metadata", "title_id": "slate-007", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-007/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b07sg"},
    {"asset_id": "ast-008-id-master_video", "title_id": "slate-008", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-008/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08id"},
    {"asset_id": "ast-008-id-subtitle", "title_id": "slate-008", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-008/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08id"},
    {"asset_id": "ast-008-id-artwork_poster", "title_id": "slate-008", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-008/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08id"},
    {"asset_id": "ast-008-id-artwork_banner", "title_id": "slate-008", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-008/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08id"},
    {"asset_id": "ast-008-id-metadata", "title_id": "slate-008", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-008/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08id"},
    {"asset_id": "ast-008-th-master_video", "title_id": "slate-008", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-008/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08th"},
    {"asset_id": "ast-008-th-subtitle", "title_id": "slate-008", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-008/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08th"},
    {"asset_id": "ast-008-th-artwork_poster", "title_id": "slate-008", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-008/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08th"},
    {"asset_id": "ast-008-th-artwork_banner", "title_id": "slate-008", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-008/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08th"},
    {"asset_id": "ast-008-th-metadata", "title_id": "slate-008", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-008/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08th"},
    {"asset_id": "ast-008-sg-master_video", "title_id": "slate-008", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-008/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08sg"},
    {"asset_id": "ast-008-sg-subtitle", "title_id": "slate-008", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-008/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08sg"},
    {"asset_id": "ast-008-sg-artwork_poster", "title_id": "slate-008", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-008/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08sg"},
    {"asset_id": "ast-008-sg-artwork_banner", "title_id": "slate-008", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-008/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08sg"},
    {"asset_id": "ast-008-sg-metadata", "title_id": "slate-008", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-008/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b08sg"},
    {"asset_id": "ast-009-id-master_video", "title_id": "slate-009", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-009/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09id"},
    {"asset_id": "ast-009-id-subtitle", "title_id": "slate-009", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-009/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09id"},
    {"asset_id": "ast-009-id-artwork_poster", "title_id": "slate-009", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-009/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09id"},
    {"asset_id": "ast-009-id-artwork_banner", "title_id": "slate-009", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-009/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09id"},
    {"asset_id": "ast-009-id-metadata", "title_id": "slate-009", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-009/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09id"},
    {"asset_id": "ast-009-th-master_video", "title_id": "slate-009", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-009/th/master_video.bin", "qc_status": "failed", "qc_notes": "Frame rate mismatch: 25.0fps submitted, required 23.976fps / 1080p24", "checksum": "sha256:b09th"},
    {"asset_id": "ast-009-th-subtitle", "title_id": "slate-009", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-009/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09th"},
    {"asset_id": "ast-009-th-artwork_poster", "title_id": "slate-009", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-009/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09th"},
    {"asset_id": "ast-009-th-artwork_banner", "title_id": "slate-009", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-009/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09th"},
    {"asset_id": "ast-009-th-metadata", "title_id": "slate-009", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-009/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09th"},
    {"asset_id": "ast-009-sg-master_video", "title_id": "slate-009", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-009/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09sg"},
    {"asset_id": "ast-009-sg-subtitle", "title_id": "slate-009", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-009/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09sg"},
    {"asset_id": "ast-009-sg-artwork_poster", "title_id": "slate-009", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-009/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09sg"},
    {"asset_id": "ast-009-sg-artwork_banner", "title_id": "slate-009", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-009/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09sg"},
    {"asset_id": "ast-009-sg-metadata", "title_id": "slate-009", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-009/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b09sg"},
    {"asset_id": "ast-010-id-master_video", "title_id": "slate-010", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-010/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0aid"},
    {"asset_id": "ast-010-id-subtitle", "title_id": "slate-010", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-010/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0aid"},
    {"asset_id": "ast-010-id-artwork_poster", "title_id": "slate-010", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-010/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0aid"},
    {"asset_id": "ast-010-id-artwork_banner", "title_id": "slate-010", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-010/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0aid"},
    {"asset_id": "ast-010-id-metadata", "title_id": "slate-010", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-010/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0aid"},
    {"asset_id": "ast-010-th-master_video", "title_id": "slate-010", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-010/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0ath"},
    {"asset_id": "ast-010-th-subtitle", "title_id": "slate-010", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-010/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0ath"},
    {"asset_id": "ast-010-th-artwork_poster", "title_id": "slate-010", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-010/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0ath"},
    {"asset_id": "ast-010-th-artwork_banner", "title_id": "slate-010", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-010/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0ath"},
    {"asset_id": "ast-010-th-metadata", "title_id": "slate-010", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-010/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0ath"},
    {"asset_id": "ast-010-sg-master_video", "title_id": "slate-010", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-010/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0asg"},
    {"asset_id": "ast-010-sg-subtitle", "title_id": "slate-010", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-010/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0asg"},
    {"asset_id": "ast-010-sg-artwork_poster", "title_id": "slate-010", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-010/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0asg"},
    {"asset_id": "ast-010-sg-artwork_banner", "title_id": "slate-010", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-010/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0asg"},
    {"asset_id": "ast-010-sg-metadata", "title_id": "slate-010", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-010/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0asg"},
    {"asset_id": "ast-011-id-master_video", "title_id": "slate-011", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-011/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bid"},
    {"asset_id": "ast-011-id-subtitle", "title_id": "slate-011", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-011/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bid"},
    {"asset_id": "ast-011-id-artwork_poster", "title_id": "slate-011", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-011/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bid"},
    {"asset_id": "ast-011-id-artwork_banner", "title_id": "slate-011", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-011/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bid"},
    {"asset_id": "ast-011-id-metadata", "title_id": "slate-011", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-011/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bid"},
    {"asset_id": "ast-011-th-master_video", "title_id": "slate-011", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-011/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bth"},
    {"asset_id": "ast-011-th-subtitle", "title_id": "slate-011", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-011/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bth"},
    {"asset_id": "ast-011-th-artwork_poster", "title_id": "slate-011", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-011/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bth"},
    {"asset_id": "ast-011-th-artwork_banner", "title_id": "slate-011", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-011/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bth"},
    {"asset_id": "ast-011-th-metadata", "title_id": "slate-011", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-011/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bth"},
    {"asset_id": "ast-011-sg-master_video", "title_id": "slate-011", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-011/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bsg"},
    {"asset_id": "ast-011-sg-subtitle", "title_id": "slate-011", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-011/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bsg"},
    {"asset_id": "ast-011-sg-artwork_poster", "title_id": "slate-011", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-011/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bsg"},
    {"asset_id": "ast-011-sg-artwork_banner", "title_id": "slate-011", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-011/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0bsg"},
    {"asset_id": "ast-011-sg-metadata", "title_id": "slate-011", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-011/sg/metadata.bin", "qc_status": "failed", "qc_notes": "IMDA age rating certification pending distributor registration", "checksum": "sha256:b0bsg"},
    {"asset_id": "ast-012-id-master_video", "title_id": "slate-012", "territory": "ID", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-012/id/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cid"},
    {"asset_id": "ast-012-id-subtitle", "title_id": "slate-012", "territory": "ID", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-012/id/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cid"},
    {"asset_id": "ast-012-id-artwork_poster", "title_id": "slate-012", "territory": "ID", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-012/id/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cid"},
    {"asset_id": "ast-012-id-artwork_banner", "title_id": "slate-012", "territory": "ID", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-012/id/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cid"},
    {"asset_id": "ast-012-id-metadata", "title_id": "slate-012", "territory": "ID", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-012/id/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cid"},
    {"asset_id": "ast-012-th-master_video", "title_id": "slate-012", "territory": "TH", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-012/th/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cth"},
    {"asset_id": "ast-012-th-subtitle", "title_id": "slate-012", "territory": "TH", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-012/th/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cth"},
    {"asset_id": "ast-012-th-artwork_poster", "title_id": "slate-012", "territory": "TH", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-012/th/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cth"},
    {"asset_id": "ast-012-th-artwork_banner", "title_id": "slate-012", "territory": "TH", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-012/th/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cth"},
    {"asset_id": "ast-012-th-metadata", "title_id": "slate-012", "territory": "TH", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-012/th/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0cth"},
    {"asset_id": "ast-012-sg-master_video", "title_id": "slate-012", "territory": "SG", "asset_type": "master_video", "file_path": "s3://distro-sg/slate-012/sg/master_video.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0csg"},
    {"asset_id": "ast-012-sg-subtitle", "title_id": "slate-012", "territory": "SG", "asset_type": "subtitle", "file_path": "s3://distro-sg/slate-012/sg/subtitle.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0csg"},
    {"asset_id": "ast-012-sg-artwork_poster", "title_id": "slate-012", "territory": "SG", "asset_type": "artwork_poster", "file_path": "s3://distro-sg/slate-012/sg/artwork_poster.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0csg"},
    {"asset_id": "ast-012-sg-artwork_banner", "title_id": "slate-012", "territory": "SG", "asset_type": "artwork_banner", "file_path": "s3://distro-sg/slate-012/sg/artwork_banner.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0csg"},
    {"asset_id": "ast-012-sg-metadata", "title_id": "slate-012", "territory": "SG", "asset_type": "metadata", "file_path": "s3://distro-sg/slate-012/sg/metadata.bin", "qc_status": "passed", "qc_notes": "QC verified broadcast ready", "checksum": "sha256:b0csg"},
]


def query_fleet_analytics_fixtures() -> Dict[str, Any]:
    """
    Performs analytical aggregations across the entire title fleet.
    Mimics ClickHouse OLAP aggregation functions:
    countIf(qc_status = 'passed'), territory readiness, bottleneck distribution.
    """
    from app.engine.policy import evaluate_greenlight
    from datetime import date
    import time

    start_t = time.perf_counter()
    default_date = date(2026, 9, 15)
    territories = ["ID", "TH", "SG"]
    platform = "FAST"

    total_titles = len(TITLES_FIXTURE)
    green_count = 0
    amber_count = 0
    red_count = 0

    territory_pass_counts = {"ID": 0, "TH": 0, "SG": 0}
    bottleneck_counts: Dict[str, int] = {}

    for t in TITLES_FIXTURE:
        tid = t["title_id"]
        raw = query_fixtures(tid, territories, platform)
        resp = evaluate_greenlight(
            title_id=tid,
            launch_date=default_date,
            territories=territories,
            platform=platform,
            raw_data=raw,
            tool_trace=[],
            data_mode="fixture"
        )
        if resp.decision.value == "green":
            green_count += 1
        elif resp.decision.value == "amber":
            amber_count += 1
        else:
            red_count += 1

        # Check territory breakdown
        for terr in territories:
            terr_checks = [c for c in resp.checks if c.territory == terr]
            if all(c.status == "pass" for c in terr_checks):
                territory_pass_counts[terr] += 1

        # Track failure bottlenecks
        for c in resp.checks:
            if c.status != "pass":
                cat_label = c.category.replace("_", " ").title()
                bottleneck_counts[cat_label] = bottleneck_counts.get(cat_label, 0) + 1

    fleet_readiness_pct = round((green_count / total_titles) * 100.0, 1) if total_titles > 0 else 0.0
    territory_readiness = {
        terr: round((count / total_titles) * 100.0, 1)
        for terr, count in territory_pass_counts.items()
    }

    bottleneck_distribution = [
        {"category": cat, "failure_count": cnt, "share_pct": round((cnt / sum(bottleneck_counts.values())) * 100.0, 1)}
        for cat, cnt in sorted(bottleneck_counts.items(), key=lambda x: x[1], reverse=True)
    ] if bottleneck_counts else []

    total_assets = len(ASSETS_FIXTURE)
    passed_assets = sum(1 for a in ASSETS_FIXTURE if a.get("qc_status") == "passed")
    qc_pass_rate_pct = round((passed_assets / total_assets) * 100.0, 1) if total_assets > 0 else 0.0

    execution_time_ms = round((time.perf_counter() - start_t) * 1000.0, 2)

    return {
        "total_titles": total_titles,
        "green_count": green_count,
        "amber_count": amber_count,
        "red_count": red_count,
        "fleet_readiness_pct": fleet_readiness_pct,
        "territory_readiness": territory_readiness,
        "bottleneck_distribution": bottleneck_distribution,
        "total_assets": total_assets,
        "qc_pass_rate_pct": qc_pass_rate_pct,
        "execution_time_ms": execution_time_ms,
        "data_mode": "fixture",
        "tool_trace": [
            "fixture.query:fleet_readiness_olap",
            "fixture.query:territory_aggregation",
            "fixture.query:bottleneck_distribution"
        ]
    }


def query_fixtures(
    title_id: str,
    territories: List[str],
    platform: str,
) -> Dict[str, Any]:
    """
    Simulates database query retrieval using local fixtures.
    """
    title_meta = next((t for t in TITLES_FIXTURE if t["title_id"] == title_id), None)
    
    rights = [
        r for r in RIGHTS_WINDOWS_FIXTURE
        if r["title_id"] == title_id
        and r["territory"] in territories
        and r["platform"].upper() == platform.upper()
    ]

    deliverables = [
        d for d in REQUIRED_DELIVERABLES_FIXTURE
        if d["territory"] in territories
        and d["platform"].upper() == platform.upper()
    ]

    assets = [
        a for a in ASSETS_FIXTURE
        if a["title_id"] == title_id
        and a["territory"] in territories
    ]

    return {
        "title": title_meta,
        "rights": rights,
        "deliverables": deliverables,
        "assets": assets,
    }
