"""
Greenlight API Response Schemas.
"""

from enum import Enum
from typing import List, Optional
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
