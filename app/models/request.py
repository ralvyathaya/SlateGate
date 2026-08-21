"""
Greenlight API Request Schemas.
"""

from datetime import date
from typing import List, Literal, Optional
from pydantic import BaseModel, Field, field_validator


VALID_TERRITORIES = {"ID", "TH", "SG", "MY", "PH", "VN"}


class GreenlightRequest(BaseModel):
    title_id: str = Field(
        ...,
        description="Unique title identifier in catalog (e.g. 'slate-001')",
        examples=["slate-001", "slate-002", "slate-003", "slate-004"],
        pattern=r"^[a-zA-Z0-9_\-]+$",
        min_length=1,
        max_length=64,
    )
    launch_date: date = Field(
        ...,
        description="Target distribution launch date (YYYY-MM-DD)",
        examples=["2026-09-15"],
    )
    territories: List[str] = Field(
        default=["ID", "TH", "SG"],
        description="List of target launch territory ISO codes",
        examples=[["ID", "TH", "SG"]],
        min_length=1,
    )
    platform: str = Field(
        default="FAST",
        description="Target distribution platform (e.g. 'FAST')",
        examples=["FAST"],
        min_length=1,
        max_length=32,
    )
    force_data_mode: Optional[Literal["auto", "clickhouse-mcp", "fixture"]] = Field(
        default=None,
        description="Explicit override for query data mode (auto, clickhouse-mcp, fixture)",
    )

    @field_validator("territories")
    @classmethod
    def validate_territories(cls, v: List[str]) -> List[str]:
        if not v:
            raise ValueError("Territories list cannot be empty.")
        normalized = [t.upper().strip() for t in v]
        for t in normalized:
            if t not in VALID_TERRITORIES:
                raise ValueError(
                    f"Unsupported territory '{t}'. Supported territories are: {sorted(list(VALID_TERRITORIES))}"
                )
        # Deduplicate while preserving order
        return list(dict.fromkeys(normalized))

    @field_validator("platform")
    @classmethod
    def validate_platform(cls, v: str) -> str:
        cleaned = v.strip().upper()
        if not cleaned:
            raise ValueError("Platform must not be blank.")
        return cleaned

    @field_validator("title_id")
    @classmethod
    def validate_title_id(cls, v: str) -> str:
        cleaned = v.strip().lower()
        if not cleaned:
            raise ValueError("title_id must not be empty.")
        return cleaned
