from app.integrations.postgres.client import PostgresClient


def register_tools(mcp: object, client: PostgresClient) -> list[str]:
    @mcp.tool(name="postgres_health")
    def postgres_health() -> dict[str, object]:
        """Return basic health metadata for the configured Postgres connection."""
        return client.health()

    @mcp.tool(name="postgres_list_schemas")
    def postgres_list_schemas() -> dict[str, object]:
        """List application schemas visible to the configured Postgres user."""
        return {"schemas": client.list_schemas()}

    @mcp.tool(name="postgres_list_tables")
    def postgres_list_tables(schema: str | None = None) -> dict[str, object]:
        """List tables for all schemas or a specific schema."""
        return {
            "tables": client.list_tables(schema=schema),
        }

    @mcp.tool(name="postgres_describe_table")
    def postgres_describe_table(schema: str, table: str) -> dict[str, object]:
        """Describe columns for a table in the configured Postgres database."""
        return {
            "schema": schema,
            "table": table,
            "columns": client.describe_table(schema=schema, table=table),
        }

    @mcp.tool(name="postgres_query")
    def postgres_query(sql: str, row_limit: int | None = None) -> dict[str, object]:
        """Run a bounded read-only SQL query against Postgres."""
        return client.query(sql=sql, row_limit=row_limit)

    return [
        "postgres_health",
        "postgres_list_schemas",
        "postgres_list_tables",
        "postgres_describe_table",
        "postgres_query",
    ]
