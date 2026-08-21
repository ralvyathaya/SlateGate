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
]


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
