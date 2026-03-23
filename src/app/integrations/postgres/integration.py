from app.integrations.postgres.client import PostgresClient
from app.integrations.postgres.tools import register_tools
from app.types import AppContext, IntegrationRegistration


class PostgresIntegration:
    name = "postgres"

    def register(self, mcp: object, context: AppContext) -> IntegrationRegistration:
        client = PostgresClient(settings=context.settings)
        metadata = {
            "statement_timeout_ms": context.settings.postgres_statement_timeout_ms,
            "default_row_limit": context.settings.postgres_default_row_limit,
            "max_row_limit": context.settings.postgres_max_row_limit,
        }

        if context.settings.postgres_validate_on_startup:
            metadata["startup_health"] = client.health()

        tool_names = register_tools(mcp, client)
        return IntegrationRegistration(
            name=self.name,
            enabled=True,
            tool_names=tool_names,
            metadata=metadata,
        )
