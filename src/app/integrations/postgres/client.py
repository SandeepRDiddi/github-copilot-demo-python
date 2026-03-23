from datetime import date, datetime, time
from decimal import Decimal
from typing import Any
from uuid import UUID

from app.config import Settings
from app.shared.sql import validate_read_only_sql


class PostgresClient:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings

    def _connect(self):
        import psycopg
        from psycopg.rows import dict_row

        return psycopg.connect(
            self._settings.postgres_dsn,
            row_factory=dict_row,
            connect_timeout=self._settings.postgres_connect_timeout_seconds,
            autocommit=False,
        )

    def _serialize_value(self, value: Any) -> Any:
        if isinstance(value, (datetime, date, time, Decimal, UUID)):
            return str(value)
        if isinstance(value, list):
            return [self._serialize_value(item) for item in value]
        if isinstance(value, dict):
            return {key: self._serialize_value(item) for key, item in value.items()}
        return value

    def _apply_session_settings(self, cursor: Any) -> None:
        cursor.execute("SET TRANSACTION READ ONLY")
        cursor.execute(
            "SET LOCAL statement_timeout = %s",
            (self._settings.postgres_statement_timeout_ms,),
        )

    def health(self) -> dict[str, Any]:
        with self._connect() as connection:
            with connection.cursor() as cursor:
                self._apply_session_settings(cursor)
                cursor.execute("SELECT current_database() AS database, current_user AS user")
                result = cursor.fetchone()
            connection.rollback()

        return {
            "database": result["database"],
            "user": result["user"],
            "statement_timeout_ms": self._settings.postgres_statement_timeout_ms,
        }

    def list_schemas(self) -> list[dict[str, Any]]:
        sql = """
        SELECT schema_name
        FROM information_schema.schemata
        WHERE schema_name NOT IN ('pg_catalog', 'information_schema')
        ORDER BY schema_name
        """
        return self.query(sql, row_limit=self._settings.postgres_max_row_limit)["rows"]

    def list_tables(self, schema: str | None = None) -> list[dict[str, Any]]:
        sql = """
        SELECT table_schema, table_name, table_type
        FROM information_schema.tables
        WHERE table_schema NOT IN ('pg_catalog', 'information_schema')
          AND (%s IS NULL OR table_schema = %s)
        ORDER BY table_schema, table_name
        """
        return self.query(
            sql,
            params=(schema, schema),
            row_limit=self._settings.postgres_max_row_limit,
        )["rows"]

    def describe_table(self, schema: str, table: str) -> list[dict[str, Any]]:
        sql = """
        SELECT
          column_name,
          data_type,
          is_nullable,
          column_default
        FROM information_schema.columns
        WHERE table_schema = %s
          AND table_name = %s
        ORDER BY ordinal_position
        """
        return self.query(
            sql,
            params=(schema, table),
            row_limit=self._settings.postgres_max_row_limit,
        )["rows"]

    def query(
        self,
        sql: str,
        *,
        params: tuple[Any, ...] | None = None,
        row_limit: int | None = None,
    ) -> dict[str, Any]:
        validated_sql = validate_read_only_sql(sql)
        effective_limit = row_limit or self._settings.postgres_default_row_limit
        effective_limit = min(effective_limit, self._settings.postgres_max_row_limit)
        lowered_sql = validated_sql.lower()

        if lowered_sql.startswith("explain"):
            executable_sql = validated_sql
            query_params = tuple(params or ())
        else:
            executable_sql = f"SELECT * FROM ({validated_sql}) AS mcp_query LIMIT %s"
            query_params = tuple(params or ()) + (effective_limit,)

        with self._connect() as connection:
            with connection.cursor() as cursor:
                self._apply_session_settings(cursor)
                cursor.execute(executable_sql, query_params)
                rows = cursor.fetchall()
            connection.rollback()

        serialized_rows = [
            {key: self._serialize_value(value) for key, value in row.items()}
            for row in rows
        ]

        return {
            "row_count": len(serialized_rows),
            "row_limit": effective_limit,
            "rows": serialized_rows,
        }
