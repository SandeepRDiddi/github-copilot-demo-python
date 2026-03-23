import pytest

from app.config import Settings


def test_settings_require_github_token_when_enabled() -> None:
    with pytest.raises(ValueError, match="MCP_GITHUB_TOKEN"):
        Settings(
            workspace_root=".",
            github_enabled=True,
            slack_enabled=False,
        )


def test_settings_require_existing_workspace_root() -> None:
    with pytest.raises(ValueError, match="workspace_root does not exist"):
        Settings(
            workspace_root="./definitely-missing-directory",
            github_enabled=False,
            slack_enabled=False,
        )


def test_settings_require_postgres_dsn_when_enabled() -> None:
    with pytest.raises(ValueError, match="MCP_POSTGRES_DSN"):
        Settings(
            workspace_root=".",
            postgres_enabled=True,
            github_enabled=False,
            slack_enabled=False,
        )
