"""
SlateGate Application Settings and Configuration.
"""

from typing import Literal, Optional
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # App Settings
    app_env: str = "development"
    app_port: int = 8080
    app_host: str = "0.0.0.0"
    default_data_mode: Literal["auto", "clickhouse-mcp", "fixture"] = "auto"

    # Google Gemini / Vertex AI Settings
    gemini_api_key: Optional[str] = None
    gemini_model: str = "gemini-2.5-flash"
    google_cloud_project: Optional[str] = None
    google_cloud_location: str = "us-central1"

    # ClickHouse Connection Settings
    clickhouse_host: Optional[str] = None
    clickhouse_port: int = 8443
    clickhouse_user: str = "default"
    clickhouse_password: Optional[str] = None
    clickhouse_database: str = "slategate"
    clickhouse_secure: bool = True

    # ClickHouse MCP Server Configuration
    clickhouse_mcp_command: str = "uvx"
    clickhouse_mcp_package: str = "mcp-clickhouse"
    clickhouse_mcp_timeout_seconds: int = 10

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    @property
    def has_clickhouse_credentials(self) -> bool:
        """Check if ClickHouse connection details are configured."""
        return bool(self.clickhouse_host and self.clickhouse_host.strip())

    @property
    def has_gemini_credentials(self) -> bool:
        """Check if Gemini API key or GCP project is configured."""
        return bool(
            (self.gemini_api_key and self.gemini_api_key.strip())
            or (self.google_cloud_project and self.google_cloud_project.strip())
        )


settings = Settings()
