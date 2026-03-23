from pathlib import Path
from typing import Literal

from pydantic import model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="MCP_",
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    server_name: str = "Multi Integration MCP"
    environment: Literal["development", "staging", "production"] = "development"
    transport: Literal["stdio", "streamable-http", "sse"] = "stdio"
    log_level: Literal["DEBUG", "INFO", "WARNING", "ERROR"] = "INFO"
    workspace_enabled: bool = True
    workspace_root: Path = Path.cwd()
    workspace_exclude_hidden: bool = True
    workspace_max_entries: int = 100
    workspace_max_read_chars: int = 20000

    postgres_enabled: bool = False
    postgres_dsn: str | None = None
    postgres_connect_timeout_seconds: int = 10
    postgres_statement_timeout_ms: int = 15000
    postgres_default_row_limit: int = 200
    postgres_max_row_limit: int = 1000
    postgres_validate_on_startup: bool = True

    github_enabled: bool = False
    github_token: str | None = None

    slack_enabled: bool = False
    slack_bot_token: str | None = None

    @model_validator(mode="after")
    def validate_configuration(self) -> "Settings":
        self.workspace_root = self.workspace_root.resolve()

        if not self.workspace_root.exists():
            raise ValueError(f"workspace_root does not exist: {self.workspace_root}")
        if not self.workspace_root.is_dir():
            raise ValueError(f"workspace_root is not a directory: {self.workspace_root}")
        if self.workspace_max_entries < 1:
            raise ValueError("workspace_max_entries must be at least 1")
        if self.workspace_max_read_chars < 1:
            raise ValueError("workspace_max_read_chars must be at least 1")
        if self.postgres_enabled and not self.postgres_dsn:
            raise ValueError("postgres_enabled=true requires MCP_POSTGRES_DSN")
        if self.postgres_connect_timeout_seconds < 1:
            raise ValueError("postgres_connect_timeout_seconds must be at least 1")
        if self.postgres_statement_timeout_ms < 100:
            raise ValueError("postgres_statement_timeout_ms must be at least 100")
        if self.postgres_default_row_limit < 1:
            raise ValueError("postgres_default_row_limit must be at least 1")
        if self.postgres_max_row_limit < self.postgres_default_row_limit:
            raise ValueError("postgres_max_row_limit must be greater than or equal to postgres_default_row_limit")
        if self.github_enabled and not self.github_token:
            raise ValueError("github_enabled=true requires MCP_GITHUB_TOKEN")
        if self.slack_enabled and not self.slack_bot_token:
            raise ValueError("slack_enabled=true requires MCP_SLACK_BOT_TOKEN")

        return self


settings = Settings()
