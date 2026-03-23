from app.config import Settings
from app.registry import get_enabled_integrations, register_integrations
from app.types import AppContext


class FakeMCP:
    def __init__(self) -> None:
        self.tool_names: list[str] = []

    def tool(self, name: str):
        def decorator(func):
            self.tool_names.append(name)
            return func

        return decorator


def test_enabled_integrations_follow_settings() -> None:
    settings = Settings(
        workspace_root=".",
        workspace_enabled=False,
        postgres_enabled=True,
        postgres_dsn="postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable",
        postgres_validate_on_startup=False,
        github_enabled=True,
        github_token="token",
        slack_enabled=False,
    )
    context = AppContext.create(settings=settings)

    integrations = get_enabled_integrations(context)

    assert [integration.name for integration in integrations] == ["postgres", "github"]


def test_register_integrations_adds_tools_for_enabled_modules() -> None:
    settings = Settings(
        workspace_root=".",
        workspace_enabled=True,
        postgres_enabled=True,
        postgres_dsn="postgresql://postgres:postgres@localhost:5432/postgres?sslmode=disable",
        postgres_validate_on_startup=False,
        github_enabled=True,
        github_token="token",
        slack_enabled=True,
        slack_bot_token="token",
    )
    context = AppContext.create(settings=settings)
    mcp = FakeMCP()

    registered = register_integrations(mcp, context)

    assert [integration.name for integration in registered] == ["workspace", "postgres", "github", "slack"]
    assert "workspace_list_files" in mcp.tool_names
    assert "workspace_read_text_file" in mcp.tool_names
    assert "postgres_health" in mcp.tool_names
    assert "postgres_query" in mcp.tool_names
    assert "github_list_repositories" in mcp.tool_names
    assert "slack_post_message" in mcp.tool_names
