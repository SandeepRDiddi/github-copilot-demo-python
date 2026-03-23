import logging

from mcp.server.fastmcp import FastMCP

from app.config import settings
from app.logging import configure_logging
from app.registry import register_integrations
from app.types import AppContext

logger = logging.getLogger(__name__)
SERVER_VERSION = "0.1.0"


def create_server() -> FastMCP:
    context = AppContext.create(settings=settings)
    mcp = FastMCP(settings.server_name)
    registered = register_integrations(mcp, context)
    registered_names = [item.name for item in registered]

    @mcp.tool(name="server_status")
    def server_status() -> dict[str, object]:
        """Return basic metadata about the running MCP server."""
        return {
            "version": SERVER_VERSION,
            "name": settings.server_name,
            "environment": settings.environment,
            "transport": settings.transport,
            "started_at": context.started_at.isoformat(),
            "workspace_root": settings.workspace_root.as_posix(),
            "registered_integrations": registered_names,
            "integration_details": [
                {
                    "name": item.name,
                    "enabled": item.enabled,
                    "tool_names": item.tool_names,
                    "metadata": item.metadata,
                }
                for item in registered
            ],
        }

    @mcp.tool(name="list_integrations")
    def list_integrations() -> dict[str, object]:
        """Return the integrations registered on this MCP server."""
        return {
            "integrations": registered_names,
            "count": len(registered_names),
        }

    @mcp.tool(name="server_health")
    def server_health() -> dict[str, object]:
        """Return a simple readiness view for operational checks."""
        return {
            "status": "ok",
            "environment": settings.environment,
            "integration_count": len(registered_names),
            "transport": settings.transport,
        }

    logger.info("registered integrations: %s", ", ".join(registered_names) or "none")
    return mcp


def main() -> None:
    configure_logging(settings.log_level)
    server = create_server()
    server.run(transport=settings.transport)


if __name__ == "__main__":
    main()
