"""
Greenlight API Response Schemas.
"""

from enum import Enum
from typing import Any, Dict, List, Optional
from pydantic import BaseModel, Field


class DecisionEnum(str, Enum):
    GREEN = "green"
    AMBER = "amber"
    RED = "red"


class CheckCategory(str, Enum):
    RIGHTS = "rights"
    MASTER_VIDEO = "master_video"
    SUBTITLE = "subtitle"
    ARTWORK = "artwork"
    METADATA = "metadata"
    DELIVERABLES = "deliverables"


class CheckStatus(str, Enum):
    PASS = "pass"
    FAIL = "fail"
    WARNING = "warning"


class CheckItem(BaseModel):
    category: str = Field(
        ...,
        description="Check category (rights, master_video, subtitle, artwork_poster, artwork_banner, metadata)",
    )
    territory: str = Field(
        ...,
        description="Territory ISO code (e.g. 'ID', 'TH', 'SG')",
    )
    status: str = Field(
        ...,
        description="Evaluation outcome ('pass' or 'fail')",
    )
    reason: str = Field(
        ...,
        description="Human and machine-readable explanation of check outcome",
    )
    evidence: List[str] = Field(
        default_factory=list,
        description="Traceable evidence URIs/keys (e.g. 'rights:slate-001:TH:contract-slate-001-th')",
    )
    owner: str = Field(
        ...,
        description="Department or team responsible for this item (e.g. 'Rights & Licensing', 'Technical Operations')",
    )
    next_action: str = Field(
        ...,
        description="Actionable next step required to remediate or confirm status",
    )


class GreenlightResponse(BaseModel):
    decision: DecisionEnum = Field(
        ...,
        description="Final greenlight decision: green (launch ready), amber (minor blockers), red (blocked)",
    )
    summary: str = Field(
        ...,
        description="Executive summary of the launch readiness decision",
    )
    checks: List[CheckItem] = Field(
        default_factory=list,
        description="Itemized check breakdown by territory and category",
    )
    tool_trace: List[str] = Field(
        default_factory=list,
        description="Provenance of runtime tool execution steps",
    )
    data_mode: str = Field(
        ...,
        description="Data execution mode ('clickhouse-mcp' or 'fixture')",
    )
    passed_count: int = Field(
        default=0,
        description="Count of passing checks",
    )
    failed_count: int = Field(
        default=0,
        description="Count of failing checks",
    )
    total_count: int = Field(
        default=0,
        description="Total checks evaluated",
    )
    title_id: str = Field(
        ...,
        description="Evaluated title identifier",
    )
    launch_date: str = Field(
        ...,
        description="Evaluated launch date",
    )
    territories: List[str] = Field(
        ...,
        description="Evaluated territories",
    )
    platform: str = Field(
        ...,
        description="Evaluated platform",
    )
    execution_time_ms: float = Field(
        default=0.0,
        description="Query and policy evaluation latency in milliseconds",
    )


class RemediationResponse(BaseModel):
    remediation_id: str = Field(..., description="Unique remediation action reference")
    title_id: str = Field(..., description="Target title identifier")
    territory: str = Field(..., description="Target territory code")
    category: str = Field(..., description="Check category requiring remediation")
    action_type: str = Field(..., description="Remediation category (e.g. ffmpeg_loudness, licensing_addendum, vendor_dispatch)")
    work_order_title: str = Field(..., description="Official work order headline")
    work_order_content: str = Field(..., description="Synthesized operational instructions / draft memo")
    cli_command: Optional[str] = Field(default=None, description="Actionable CLI command (e.g. FFmpeg loudness filter)")
    assigned_team: str = Field(..., description="Department or vendor assigned")
    priority: str = Field(..., description="Urgency level")
    estimated_turnaround: str = Field(..., description="Expected resolution time")
    tool_trace: List[str] = Field(default_factory=list, description="Remediation tool provenance")


class FleetAnalyticsResponse(BaseModel):
    total_titles: int = Field(..., description="Total titles indexed in catalog")
    green_count: int = Field(..., description="Titles with 100% GREEN launch readiness")
    amber_count: int = Field(..., description="Titles conditionally approved (AMBER)")
    red_count: int = Field(..., description="Titles blocked (RED)")
    fleet_readiness_pct: float = Field(..., description="Percentage of titles ready for broadcast")
    territory_readiness: Dict[str, float] = Field(..., description="Readiness percentage per territory (ID, TH, SG)")
    bottleneck_distribution: List[Dict[str, Any]] = Field(..., description="Top blocker categories across catalog")
    total_assets: int = Field(..., description="Total media assets tracked in catalog")
    qc_pass_rate_pct: float = Field(..., description="Overall asset technical QC pass rate")
    execution_time_ms: float = Field(..., description="ClickHouse analytical aggregation latency in ms")
    data_mode: str = Field(..., description="ClickHouse execution mode (clickhouse-mcp or fixture)")
    tool_trace: List[str] = Field(default_factory=list, description="Tool execution trace")
