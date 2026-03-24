from datetime import datetime

from app.config import Settings
from app.server import SERVER_VERSION, create_server
from app.types import IntegrationRegistration


class FakeMCP:
    def __init__(self, name: str) -> None:
        self.name = name
        self.tool_names: list[str] = []
        self.tools: dict[str, object] = {}

    def tool(self, name: str):
        def decorator(func):
            self.tool_names.append(name)
            self.tools[name] = func
            return func

        return decorator


def test_create_server_uses_explicit_settings(monkeypatch) -> None:
    test_settings = Settings(
        workspace_root=".",
        server_name="Test MCP",
        environment="staging",
        transport="sse",
        github_enabled=False,
        slack_enabled=False,
    )

    def fake_register_integrations(mcp: FakeMCP, context):
        assert context.settings is test_settings
        return [
            IntegrationRegistration(
                name="workspace",
                enabled=True,
                tool_names=["workspace_list_files"],
                metadata={"root": context.settings.workspace_root.as_posix()},
            )
        ]

    monkeypatch.setattr("app.server.FastMCP", FakeMCP)
    monkeypatch.setattr("app.server.register_integrations", fake_register_integrations)

    server = create_server(test_settings)

    assert server.name == "Test MCP"
    assert server.tool_names == ["server_status", "list_integrations", "server_health"]

    status = server.tools["server_status"]()
    integrations = server.tools["list_integrations"]()
    health = server.tools["server_health"]()

    assert status["version"] == SERVER_VERSION
    assert status["name"] == "Test MCP"
    assert status["environment"] == "staging"
    assert status["transport"] == "sse"
    assert status["workspace_root"] == test_settings.workspace_root.resolve().as_posix()
    assert status["registered_integrations"] == ["workspace"]
    assert status["integration_details"] == [
        {
            "name": "workspace",
            "enabled": True,
            "tool_names": ["workspace_list_files"],
            "metadata": {"root": test_settings.workspace_root.resolve().as_posix()},
        }
    ]
    assert datetime.fromisoformat(status["started_at"])

    assert integrations == {
        "integrations": ["workspace"],
        "count": 1,
    }
    assert health == {
        "status": "ok",
        "environment": "staging",
        "integration_count": 1,
        "transport": "sse",
    }


def test_create_server_handles_no_registered_integrations(monkeypatch) -> None:
    test_settings = Settings(
        workspace_root=".",
        workspace_enabled=False,
        github_enabled=False,
        slack_enabled=False,
    )

    monkeypatch.setattr("app.server.FastMCP", FakeMCP)
    monkeypatch.setattr("app.server.register_integrations", lambda mcp, context: [])

    server = create_server(test_settings)

    assert server.tools["list_integrations"]() == {"integrations": [], "count": 0}
    assert server.tools["server_health"]()["integration_count"] == 0
