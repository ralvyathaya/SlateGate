-- ============================================================================
-- SlateGate — ClickHouse Seed Data
-- Fictional Southeast Asian Content Scenarios (ID, TH, SG) for FAST Platforms
-- ============================================================================

-- ----------------------------------------------------------------------------
-- 1. Titles Catalog
-- ----------------------------------------------------------------------------
INSERT INTO slategate.titles (title_id, title_name, original_language, genre, runtime_minutes, release_year, synopsis) VALUES
('slate-001', 'The Nusantara Heist', 'id', 'Action / Heist', 114, 2025, 'A daring crew of elite hackers and operatives plan a high-stakes museum heist across Jakarta, Bangkok, and Singapore.'),
('slate-002', 'Singa City Beats', 'en', 'Music / Drama', 98, 2026, 'An underground electronic music producer in Singapore navigates cross-border festivals in Southeast Asia while overcoming family expectations.'),
('slate-003', 'Bangkok Neon Nights', 'th', 'Neo-Noir / Crime', 105, 2025, 'A detective uncovers a syndicate controlling deepwater trade channels along the Chao Phraya river under the city neon glow.'),
('slate-004', 'Java Horizon', 'id', 'Adventure / Romance', 122, 2026, 'Two documentary filmmakers traverse the volcanic ridges of East Java in search of an ancient spice route legend.');

-- ----------------------------------------------------------------------------
-- 2. Required Deliverables for Platform 'FAST'
-- Mandatory: master_video, subtitle, artwork_poster, artwork_banner, metadata
-- ----------------------------------------------------------------------------
INSERT INTO slategate.required_deliverables (requirement_id, platform, territory, asset_type, is_mandatory, spec_details) VALUES
('req-fast-id-master', 'FAST', 'ID', 'master_video', 1, 'ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)'),
('req-fast-id-sub', 'FAST', 'ID', 'subtitle', 1, 'Bahasa Indonesia localized SRT/VTT (UTF-8)'),
('req-fast-id-poster', 'FAST', 'ID', 'artwork_poster', 1, '2:3 Portrait Key Art 2000x3000 JPG/PNG with localized title treatment'),
('req-fast-id-banner', 'FAST', 'ID', 'artwork_banner', 1, '16:9 Landscape Hero Banner 3840x2160 JPG'),
('req-fast-id-meta', 'FAST', 'ID', 'metadata', 1, 'Localized Indonesian title, synopsis, cast, content rating'),

('req-fast-th-master', 'FAST', 'TH', 'master_video', 1, 'ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)'),
('req-fast-th-sub', 'FAST', 'TH', 'subtitle', 1, 'Thai localized SRT/VTT (UTF-8)'),
('req-fast-th-poster', 'FAST', 'TH', 'artwork_poster', 1, '2:3 Portrait Key Art 2000x3000 JPG/PNG with localized title treatment'),
('req-fast-th-banner', 'FAST', 'TH', 'artwork_banner', 1, '16:9 Landscape Hero Banner 3840x2160 JPG'),
('req-fast-th-meta', 'FAST', 'TH', 'metadata', 1, 'Localized Thai title, synopsis, cast, content rating'),

('req-fast-sg-master', 'FAST', 'SG', 'master_video', 1, 'ProRes 422 HQ / 1080p24 / Stereo EBU R128 (-24 LUFS)'),
('req-fast-sg-sub', 'FAST', 'SG', 'subtitle', 1, 'English / Simplified Chinese SRT/VTT (UTF-8)'),
('req-fast-sg-poster', 'FAST', 'SG', 'artwork_poster', 1, '2:3 Portrait Key Art 2000x3000 JPG/PNG with bilingual title treatment'),
('req-fast-sg-banner', 'FAST', 'SG', 'artwork_banner', 1, '16:9 Landscape Hero Banner 3840x2160 JPG'),
('req-fast-sg-meta', 'FAST', 'SG', 'metadata', 1, 'Localized English / Chinese title, synopsis, IMDA rating');

-- ----------------------------------------------------------------------------
-- 3. Rights Windows
-- ----------------------------------------------------------------------------
-- slate-001: TH rights EXPIRED on 2026-06-30 (Launch date: 2026-09-15)
INSERT INTO slategate.rights_windows (rights_id, title_id, territory, platform, start_date, end_date, exclusive, contract_ref, has_conflict, conflict_notes) VALUES
('rw-001-id', 'slate-001', 'ID', 'FAST', '2026-01-01', '2027-12-31', 1, 'contract-slate-001-id', 0, ''),
('rw-001-th', 'slate-001', 'TH', 'FAST', '2025-01-01', '2026-06-30', 1, 'contract-slate-001-th', 0, 'Window lapsed without option exercise'),
('rw-001-sg', 'slate-001', 'SG', 'FAST', '2026-01-01', '2027-12-31', 1, 'contract-slate-001-sg', 0, '');

-- slate-002: Fully valid rights across ID, TH, SG (2026-01-01 to 2028-12-31)
INSERT INTO slategate.rights_windows (rights_id, title_id, territory, platform, start_date, end_date, exclusive, contract_ref, has_conflict, conflict_notes) VALUES
('rw-002-id', 'slate-002', 'ID', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-002-id', 0, ''),
('rw-002-th', 'slate-002', 'TH', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-002-th', 0, ''),
('rw-002-sg', 'slate-002', 'SG', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-002-sg', 0, '');

-- slate-003: Fully valid rights across ID, TH, SG (2026-01-01 to 2027-12-31)
INSERT INTO slategate.rights_windows (rights_id, title_id, territory, platform, start_date, end_date, exclusive, contract_ref, has_conflict, conflict_notes) VALUES
('rw-003-id', 'slate-003', 'ID', 'FAST', '2026-01-01', '2027-12-31', 1, 'contract-slate-003-id', 0, ''),
('rw-003-th', 'slate-003', 'TH', 'FAST', '2026-01-01', '2027-12-31', 1, 'contract-slate-003-th', 0, ''),
('rw-003-sg', 'slate-003', 'SG', 'FAST', '2026-01-01', '2027-12-31', 1, 'contract-slate-003-sg', 0, '');

-- slate-004: Fully valid rights across ID, TH, SG (2026-01-01 to 2028-12-31)
INSERT INTO slategate.rights_windows (rights_id, title_id, territory, platform, start_date, end_date, exclusive, contract_ref, has_conflict, conflict_notes) VALUES
('rw-004-id', 'slate-004', 'ID', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-004-id', 0, ''),
('rw-004-th', 'slate-004', 'TH', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-004-th', 0, ''),
('rw-004-sg', 'slate-004', 'SG', 'FAST', '2026-01-01', '2028-12-31', 1, 'contract-slate-004-sg', 0, '');

-- ----------------------------------------------------------------------------
-- 4. Assets & QC Inventory
-- ----------------------------------------------------------------------------

-- slate-001: Master passed, but ID subtitle missing & TH artwork poster missing
INSERT INTO slategate.assets (asset_id, title_id, territory, asset_type, file_path, qc_status, qc_notes, checksum) VALUES
('ast-001-id-mv', 'slate-001', 'ID', 'master_video', 's3://distro-sg/slate-001/id/master_1080p.mov', 'passed', 'QC clean, ProRes 422 HQ, -23.8 LUFS', 'sha256:7f9a01'),
('ast-001-id-art-b', 'slate-001', 'ID', 'artwork_banner', 's3://distro-sg/slate-001/id/hero_banner_16x9.jpg', 'passed', 'Resolution 3840x2160 confirmed', 'sha256:7f9a02'),
('ast-001-id-art-p', 'slate-001', 'ID', 'artwork_poster', 's3://distro-sg/slate-001/id/poster_2x3.jpg', 'passed', 'Resolution 2000x3000 confirmed', 'sha256:7f9a03'),
('ast-001-id-meta', 'slate-001', 'ID', 'metadata', 's3://distro-sg/slate-001/id/metadata.json', 'passed', 'Title, synopsis, age rating valid', 'sha256:7f9a04'),
-- Notice: ID subtitle is NOT present in assets table

('ast-001-th-mv', 'slate-001', 'TH', 'master_video', 's3://distro-sg/slate-001/th/master_1080p.mov', 'passed', 'QC clean, ProRes 422 HQ', 'sha256:7f9a05'),
('ast-001-th-sub', 'slate-001', 'TH', 'subtitle', 's3://distro-sg/slate-001/th/subtitles_th.srt', 'passed', 'Thai timing and glyph rendering verified', 'sha256:7f9a06'),
('ast-001-th-art-b', 'slate-001', 'TH', 'artwork_banner', 's3://distro-sg/slate-001/th/hero_banner_16x9.jpg', 'passed', 'Resolution 3840x2160 confirmed', 'sha256:7f9a07'),
('ast-001-th-meta', 'slate-001', 'TH', 'metadata', 's3://distro-sg/slate-001/th/metadata.json', 'passed', 'Thai metadata verified', 'sha256:7f9a08'),
-- Notice: TH artwork_poster is NOT present in assets table

('ast-001-sg-mv', 'slate-001', 'SG', 'master_video', 's3://distro-sg/slate-001/sg/master_1080p.mov', 'passed', 'QC clean, ProRes 422 HQ', 'sha256:7f9a09'),
('ast-001-sg-sub', 'slate-001', 'SG', 'subtitle', 's3://distro-sg/slate-001/sg/subtitles_en.srt', 'passed', 'English subtitles verified', 'sha256:7f9a10'),
('ast-001-sg-art-p', 'slate-001', 'SG', 'artwork_poster', 's3://distro-sg/slate-001/sg/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:7f9a11'),
('ast-001-sg-art-b', 'slate-001', 'SG', 'artwork_banner', 's3://distro-sg/slate-001/sg/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:7f9a12'),
('ast-001-sg-meta', 'slate-001', 'SG', 'metadata', 's3://distro-sg/slate-001/sg/metadata.json', 'passed', 'IMDA PG13 metadata verified', 'sha256:7f9a13');

-- slate-002: ALL assets present and passed QC in ID, TH, and SG
INSERT INTO slategate.assets (asset_id, title_id, territory, asset_type, file_path, qc_status, qc_notes, checksum) VALUES
('ast-002-id-mv', 'slate-002', 'ID', 'master_video', 's3://distro-sg/slate-002/id/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.1 LUFS broadcast ready', 'sha256:8b0101'),
('ast-002-id-sub', 'slate-002', 'ID', 'subtitle', 's3://distro-sg/slate-002/id/subtitles_id.srt', 'passed', 'Bahasa Indonesia UTF-8 certified', 'sha256:8b0102'),
('ast-002-id-art-p', 'slate-002', 'ID', 'artwork_poster', 's3://distro-sg/slate-002/id/poster_2x3.jpg', 'passed', '2000x3000 verified', 'sha256:8b0103'),
('ast-002-id-art-b', 'slate-002', 'ID', 'artwork_banner', 's3://distro-sg/slate-002/id/hero_banner_16x9.jpg', 'passed', '3840x2160 verified', 'sha256:8b0104'),
('ast-002-id-meta', 'slate-002', 'ID', 'metadata', 's3://distro-sg/slate-002/id/metadata.json', 'passed', 'Complete ID metadata', 'sha256:8b0105'),

('ast-002-th-mv', 'slate-002', 'TH', 'master_video', 's3://distro-sg/slate-002/th/master_1080p.mov', 'passed', 'ProRes 422 HQ, -23.9 LUFS', 'sha256:8b0106'),
('ast-002-th-sub', 'slate-002', 'TH', 'subtitle', 's3://distro-sg/slate-002/th/subtitles_th.srt', 'passed', 'Thai UTF-8 certified', 'sha256:8b0107'),
('ast-002-th-art-p', 'slate-002', 'TH', 'artwork_poster', 's3://distro-sg/slate-002/th/poster_2x3.jpg', 'passed', '2000x3000 verified', 'sha256:8b0108'),
('ast-002-th-art-b', 'slate-002', 'TH', 'artwork_banner', 's3://distro-sg/slate-002/th/hero_banner_16x9.jpg', 'passed', '3840x2160 verified', 'sha256:8b0109'),
('ast-002-th-meta', 'slate-002', 'TH', 'metadata', 's3://distro-sg/slate-002/th/metadata.json', 'passed', 'Complete TH metadata', 'sha256:8b0110'),

('ast-002-sg-mv', 'slate-002', 'SG', 'master_video', 's3://distro-sg/slate-002/sg/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:8b0111'),
('ast-002-sg-sub', 'slate-002', 'SG', 'subtitle', 's3://distro-sg/slate-002/sg/subtitles_en.srt', 'passed', 'English/Chinese UTF-8 certified', 'sha256:8b0112'),
('ast-002-sg-art-p', 'slate-002', 'SG', 'artwork_poster', 's3://distro-sg/slate-002/sg/poster_2x3.jpg', 'passed', '2000x3000 verified', 'sha256:8b0113'),
('ast-002-sg-art-b', 'slate-002', 'SG', 'artwork_banner', 's3://distro-sg/slate-002/sg/hero_banner_16x9.jpg', 'passed', '3840x2160 verified', 'sha256:8b0114'),
('ast-002-sg-meta', 'slate-002', 'SG', 'metadata', 's3://distro-sg/slate-002/sg/metadata.json', 'passed', 'Complete SG IMDA metadata', 'sha256:8b0115');

-- slate-003: ID Master video FAILED QC (Loudness violation)
INSERT INTO slategate.assets (asset_id, title_id, territory, asset_type, file_path, qc_status, qc_notes, checksum) VALUES
('ast-003-id-mv', 'slate-003', 'ID', 'master_video', 's3://distro-sg/slate-003/id/master_1080p.mov', 'failed', 'Loudness failed: -18.2 LUFS exceeds FAST standard (-24.0 +/- 1 LUFS). Audio clipping detected at 00:42:15.', 'sha256:9c0201'),
('ast-003-id-sub', 'slate-003', 'ID', 'subtitle', 's3://distro-sg/slate-003/id/subtitles_id.srt', 'passed', 'Bahasa Indonesia subtitles verified', 'sha256:9c0202'),
('ast-003-id-art-p', 'slate-003', 'ID', 'artwork_poster', 's3://distro-sg/slate-003/id/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:9c0203'),
('ast-003-id-art-b', 'slate-003', 'ID', 'artwork_banner', 's3://distro-sg/slate-003/id/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:9c0204'),
('ast-003-id-meta', 'slate-003', 'ID', 'metadata', 's3://distro-sg/slate-003/id/metadata.json', 'passed', 'Metadata verified', 'sha256:9c0205'),

('ast-003-th-mv', 'slate-003', 'TH', 'master_video', 's3://distro-sg/slate-003/th/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:9c0206'),
('ast-003-th-sub', 'slate-003', 'TH', 'subtitle', 's3://distro-sg/slate-003/th/subtitles_th.srt', 'passed', 'Thai subtitles verified', 'sha256:9c0207'),
('ast-003-th-art-p', 'slate-003', 'TH', 'artwork_poster', 's3://distro-sg/slate-003/th/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:9c0208'),
('ast-003-th-art-b', 'slate-003', 'TH', 'artwork_banner', 's3://distro-sg/slate-003/th/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:9c0209'),
('ast-003-th-meta', 'slate-003', 'TH', 'metadata', 's3://distro-sg/slate-003/th/metadata.json', 'passed', 'Metadata verified', 'sha256:9c0210'),

('ast-003-sg-mv', 'slate-003', 'SG', 'master_video', 's3://distro-sg/slate-003/sg/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:9c0211'),
('ast-003-sg-sub', 'slate-003', 'SG', 'subtitle', 's3://distro-sg/slate-003/sg/subtitles_en.srt', 'passed', 'English subtitles verified', 'sha256:9c0212'),
('ast-003-sg-art-p', 'slate-003', 'SG', 'artwork_poster', 's3://distro-sg/slate-003/sg/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:9c0213'),
('ast-003-sg-art-b', 'slate-003', 'SG', 'artwork_banner', 's3://distro-sg/slate-003/sg/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:9c0214'),
('ast-003-sg-meta', 'slate-003', 'SG', 'metadata', 's3://distro-sg/slate-003/sg/metadata.json', 'passed', 'Metadata verified', 'sha256:9c0215');

-- slate-004: ID Subtitle MISSING, but master & all other assets passed
INSERT INTO slategate.assets (asset_id, title_id, territory, asset_type, file_path, qc_status, qc_notes, checksum) VALUES
('ast-004-id-mv', 'slate-004', 'ID', 'master_video', 's3://distro-sg/slate-004/id/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:ad0301'),
-- Notice: ID subtitle is NOT present in assets table
('ast-004-id-art-p', 'slate-004', 'ID', 'artwork_poster', 's3://distro-sg/slate-004/id/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:ad0302'),
('ast-004-id-art-b', 'slate-004', 'ID', 'artwork_banner', 's3://distro-sg/slate-004/id/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:ad0303'),
('ast-004-id-meta', 'slate-004', 'ID', 'metadata', 's3://distro-sg/slate-004/id/metadata.json', 'passed', 'Metadata verified', 'sha256:ad0304'),

('ast-004-th-mv', 'slate-004', 'TH', 'master_video', 's3://distro-sg/slate-004/th/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:ad0305'),
('ast-004-th-sub', 'slate-004', 'TH', 'subtitle', 's3://distro-sg/slate-004/th/subtitles_th.srt', 'passed', 'Thai subtitles verified', 'sha256:ad0306'),
('ast-004-th-art-p', 'slate-004', 'TH', 'artwork_poster', 's3://distro-sg/slate-004/th/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:ad0307'),
('ast-004-th-art-b', 'slate-004', 'TH', 'artwork_banner', 's3://distro-sg/slate-004/th/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:ad0308'),
('ast-004-th-meta', 'slate-004', 'TH', 'metadata', 's3://distro-sg/slate-004/th/metadata.json', 'passed', 'Metadata verified', 'sha256:ad0309'),

('ast-004-sg-mv', 'slate-004', 'SG', 'master_video', 's3://distro-sg/slate-004/sg/master_1080p.mov', 'passed', 'ProRes 422 HQ, -24.0 LUFS', 'sha256:ad0310'),
('ast-004-sg-sub', 'slate-004', 'SG', 'subtitle', 's3://distro-sg/slate-004/sg/subtitles_en.srt', 'passed', 'English subtitles verified', 'sha256:ad0311'),
('ast-004-sg-art-p', 'slate-004', 'SG', 'artwork_poster', 's3://distro-sg/slate-004/sg/poster_2x3.jpg', 'passed', 'Poster verified', 'sha256:ad0312'),
('ast-004-sg-art-b', 'slate-004', 'SG', 'artwork_banner', 's3://distro-sg/slate-004/sg/hero_banner_16x9.jpg', 'passed', 'Banner verified', 'sha256:ad0313'),
('ast-004-sg-meta', 'slate-004', 'SG', 'metadata', 's3://distro-sg/slate-004/sg/metadata.json', 'passed', 'Metadata verified', 'sha256:ad0314');
