# SlateGate — Content Greenlight Agent

> **Agentic Cinema: The Blockbuster Hackathon** — *ClickHouse Partner Track*  
> Powered by **ClickHouse Cloud / MCP**, **Google Cloud Vertex AI (Gemini 2.5 Flash)**, **Google ADK**, and **FastAPI**.

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Python 3.11+](https://img.shields.io/badge/Python-3.11%2B-blue.svg)](pyproject.toml)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.115%2B-009688.svg)](https://fastapi.tiangolo.com)
[![ClickHouse MCP](https://img.shields.io/badge/ClickHouse-MCP%20Server-FFCC00.svg)](https://github.com/ClickHouse/mcp-clickhouse)
[![Google Gemini](https://img.shields.io/badge/Google-Gemini%202.5%20Flash-4285F4.svg)](https://cloud.google.com/vertex-ai)

---

## 📌 Executive Summary

**SlateGate** is an autonomous, evidence-backed Content Greenlight Agent designed for regional media distributors and FAST (Free Ad-Supported Streaming TV) operators in Southeast Asia (**Indonesia [ID]**, **Thailand [TH]**, and **Singapore [SG]**).

Distributors frequently encounter severe launch bottlenecks, including:
- **Territory Rights Windows & Contract Conflicts**: Missing or expired territorial licenses.
- **Broadcast Master Video Specifications & Audio QC**: Non-compliant loudness (EBU R128), video artifacts, or missing reels.
- **Regional Localization**: Missing Bahasa Indonesia or Thai subtitles/captions.
- **Key Art & Platform Deliverables**: Missing 16:9 hero banners or 2:3 key art posters.
- **Localized Metadata**: Incomplete synopsis, age ratings (e.g. IMDA Singapore), or category tagging.

SlateGate queries **ClickHouse** analytical storage via the official **`mcp-clickhouse`** runtime, evaluates a strict deterministic policy hierarchy, and coordinates with **Google Gemini (Launch Director Agent)** to produce an instant, evidence-backed **GREEN**, **AMBER**, or **RED** decision with clear department owners and actionable next steps.

---

## 🏛️ Architecture & Decision Policy

### System Architecture Flow
```mermaid
flowchart TD
    subgraph ClientLayer [Operations Control Room]
        UI[Responsive Web Dashboard] --> API[FastAPI Backend /api/greenlight]
    end

    subgraph AgentLayer [Google AI Ecosystem]
        API --> Agent[Gemini Launch Director Agent]
        Agent --> Policy[Deterministic Policy Engine]
    end

    subgraph DataLayer [ClickHouse Analytical Storage]
        Policy --> MCP[Official ClickHouse MCP Client]
        MCP -->|run_query| DB[(ClickHouse Cloud Cluster)]
        DB -->|rights_windows, deliverables, assets| MCP
    end

    subgraph ResolutionLayer [Decision & Provenance]
        MCP --> Policy
        Policy --> Agent
        Agent -->|GREEN / AMBER / RED + Real Tool Trace| UI
    end
```

### Strict Decision Hierarchy
- 🔴 **RED**: Territory rights are expired, conflicting, or missing; OR required master video is missing or failed QC.
- 🟡 **AMBER**: Rights and master video are valid, but required supporting deliverables (subtitles, artwork, metadata) are missing or failed QC.
- 🟢 **GREEN**: 100% of required checks passed with verifiable evidence across all target territories.
- 🛡️ **Safety Guarantee**: Missing/incomplete database data or MCP timeouts return explicit error states, never a positive greenlight.

---

## 🎬 Canonical Fictional Scenarios

SlateGate includes 4 built-in Southeast Asian distribution scenarios:

| Title ID | Title Name | Target Date | Territories | Expected Decision | Core Finding |
| :--- | :--- | :--- | :--- | :---: | :--- |
| **`slate-001`** | *The Nusantara Heist* | 2026-09-15 | ID, TH, SG | 🔴 **RED** | Thailand rights window expired (2026-06-30); Indonesian subtitle missing; Thai artwork missing. |
| **`slate-002`** | *Singa City Beats* | 2026-09-15 | ID, TH, SG | 🟢 **GREEN** | Valid rights through 2028 and all ProRes masters, localized subtitles, key art, and metadata passed QC. |
| **`slate-003`** | *Bangkok Neon Nights* | 2026-09-15 | ID, TH, SG | 🔴 **RED** | Indonesian broadcast master video failed audio loudness QC (-18.2 LUFS vs required -24 LUFS). |
| **`slate-004`** | *Java Horizon* | 2026-09-15 | ID, TH, SG | 🟡 **AMBER** | Rights and masters valid; Bahasa Indonesia subtitle track missing from asset catalog. |

---

## 🚀 Quickstart Guide

### Prerequisites
- Python 3.11+ (tested on Python 3.12, 3.14)
- `uv` (recommended) or standard `pip`

### 1. Clone & Install Dependencies
```bash
git clone https://github.com/your-username/SlateGate.git
cd SlateGate

# Option A: Using uv (fastest)
uv venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
uv pip install -r requirements.txt

# Option B: Standard pip
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 2. Environment Configuration
Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

To run with **Live ClickHouse Cloud** and **Google Gemini**:
```ini
# .env
APP_ENV=production
APP_PORT=8080

# Google Gemini / Vertex AI
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-2.5-flash

# ClickHouse Cloud
CLICKHOUSE_HOST=your-instance.clickhouse.cloud
CLICKHOUSE_PORT=8443
CLICKHOUSE_USER=default
CLICKHOUSE_PASSWORD=your_clickhouse_password
CLICKHOUSE_DATABASE=slategate
CLICKHOUSE_SECURE=true
```

*(Note: If no credentials are configured, SlateGate automatically runs in **Demo · Synthetic Fixture Mode** with zero external dependencies).*

### 3. Run Automated Tests
```bash
pytest -v
```
*Expected: 20 passed tests verifying all scenarios, security guardrails, timeout handling, and tool trace provenance.*

### 4. Launch Local Development Server
```bash
uvicorn app.main:app --reload --port 8080
```
Open your browser at: **[http://localhost:8080](http://localhost:8080)**

---

## 🗄️ ClickHouse Database Setup & MCP Runtime

### 1. Bootstrap Database Schema and Seed Data
Execute the unified SQL script against your ClickHouse Cloud cluster or local instance:
```bash
# Using clickhouse-client CLI
clickhouse-client --host $CLICKHOUSE_HOST --user $CLICKHOUSE_USER --password $CLICKHOUSE_PASSWORD --secure --queries-file sql/00_init_all.sql

# Or using curl HTTP endpoint
curl -u $CLICKHOUSE_USER:$CLICKHOUSE_PASSWORD -sS "https://$CLICKHOUSE_HOST:$CLICKHOUSE_PORT/" --data-binary @sql/00_init_all.sql
```

### 2. Official `mcp-clickhouse` Integration
SlateGate integrates with the official [`mcp-clickhouse`](https://github.com/ClickHouse/mcp-clickhouse) server package via standard MCP protocol.

Queries are strictly read-only (`SELECT` statements only). Any modification attempt (`INSERT`, `DROP`, `ALTER`, `TRUNCATE`, `UPDATE`) is blocked by SlateGate's query safety guardrail prior to execution.

---

## ☁️ Google Cloud Run Deployment

### 1. Store Secrets in Google Secret Manager
```bash
# Create ClickHouse password secret
echo -n "your_clickhouse_password" | gcloud secrets create clickhouse-password --data-file=-

# Create Gemini API Key secret
echo -n "your_gemini_api_key" | gcloud secrets create gemini-api-key --data-file=-
```

### 2. Build and Deploy to Cloud Run
```bash
# Build container image with Google Cloud Build
gcloud builds submit --tag gcr.io/$GOOGLE_CLOUD_PROJECT/slategate:latest

# Deploy to Cloud Run with Secret Manager binding
gcloud run deploy slategate \
    --image gcr.io/$GOOGLE_CLOUD_PROJECT/slategate:latest \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \
    --set-env-vars="CLICKHOUSE_HOST=your-instance.clickhouse.cloud,CLICKHOUSE_PORT=8443,CLICKHOUSE_USER=default,CLICKHOUSE_DATABASE=slategate,CLICKHOUSE_SECURE=true,GEMINI_MODEL=gemini-2.5-flash" \
    --set-secrets="CLICKHOUSE_PASSWORD=clickhouse-password:latest,GEMINI_API_KEY=gemini-api-key:latest"
```

---

## 🎥 3-Minute Video Demo Walkthrough Script

| Time | Visual / Screen Action | Voiceover Narration |
| :--- | :--- | :--- |
| **0:00 - 0:30** | Opening dashboard; show title "SlateGate — Content Greenlight Agent" and architecture badge. | *"Welcome to SlateGate. For Southeast Asian FAST channels and regional distributors, launching a movie across Indonesia, Thailand, and Singapore is fraught with compliance risks—from expired rights to failed master QC and missing subtitles. SlateGate is an autonomous Content Greenlight Agent powered by ClickHouse MCP and Google Gemini."* |
| **0:30 - 1:00** | Click **`slate-001` ("The Nusantara Heist")** card. Click "Run Greenlight Audit". | *"Let's test our first title: 'The Nusantara Heist'. With one click, SlateGate queries ClickHouse analytical storage via the official `mcp-clickhouse` server. The result is an immediate RED decision: while Indonesian and Singapore rights are valid, Thailand rights expired in June 2026. The itemized checks table points directly to the contract reference and assigns next action to Rights & Licensing."* |
| **1:00 - 1:30** | Click **`slate-003` ("Bangkok Neon Nights")**. Click "Run Greenlight Audit". | *"Next, let's look at 'Bangkok Neon Nights'. Here, rights are active in all territories, but our technical QC check in ClickHouse flags an Indonesian broadcast master failure: audio loudness measured -18.2 LUFS, exceeding the -24 LUFS FAST standard. SlateGate blocks launch with RED and assigns remediation to Technical Operations."* |
| **1:30 - 2:00** | Click **`slate-004` ("Java Horizon")**. Click "Run Greenlight Audit". | *"Now let's check 'Java Horizon'. Rights and master videos are 100% valid, but the Bahasa Indonesia subtitle file is missing from the asset catalog. SlateGate returns AMBER: conditionally approved, with an actionable task for the Localization team."* |
| **2:00 - 2:30** | Click **`slate-002` ("Singa City Beats")**. Click "Run Greenlight Audit". | *"Finally, 'Singa City Beats'. All territory rights windows, ProRes masters, localized subtitles, key art banners, and IMDA metadata pass with flying colors. SlateGate issues a definitive GREEN launch clearance with complete tool execution trace."* |
| **2:30 - 3:00** | Highlight Tool Trace chips (`mcp-clickhouse.run_query`, `gemini.agent:launch_director`), show `/health` JSON, and conclude. | *"SlateGate provides end-to-end provenance, connecting ClickHouse's speed with Gemini's intelligence and deterministic policy guardrails. SlateGate is ready for production on Google Cloud Run."* |

---

## 🏆 Compliance Checklist

- [x] **Clean-room implementation**: Built completely from scratch without copying or deriving from earlier prototypes.
- [x] **Agentic Cinema & ClickHouse Track**: Integrates ClickHouse analytical storage and official `mcp-clickhouse` runtime.
- [x] **Google AI Ecosystem**: Exclusively uses Google Cloud Vertex AI (Gemini 2.5 Flash) and Google ADK / GenAI SDK. Zero third-party LLM frameworks.
- [x] **Deterministic Policy Enforcement**: Strict mathematical hierarchy (RED / AMBER / GREEN) with complete evidence provenance.
- [x] **Safe Error Handling**: ClickHouse / MCP timeout returns explicit HTTP 504 error, never a false positive.
- [x] **Dual Execution Modes**: Verified distinction between `Live · Gemini + ClickHouse MCP` and `Demo · Synthetic Fixture`.
- [x] **Test Coverage**: 20 automated tests passing with 100% assertion success.
- [x] **Production Deployment**: Cloud Run Dockerfile and Secret Manager integration instructions provided.

---

## 📄 License
This project is licensed under the OSI-approved **MIT License** — see the [LICENSE](LICENSE) file for details.
