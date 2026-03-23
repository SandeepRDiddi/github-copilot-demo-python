import pytest

from app.shared.sql import validate_read_only_sql


def test_validate_read_only_sql_accepts_select() -> None:
    assert validate_read_only_sql("SELECT 1") == "SELECT 1"


def test_validate_read_only_sql_blocks_mutation() -> None:
    with pytest.raises(ValueError, match="only SELECT, WITH, and EXPLAIN queries are allowed"):
        validate_read_only_sql("DELETE FROM users")


def test_validate_read_only_sql_blocks_multiple_statements() -> None:
    with pytest.raises(ValueError, match="multiple SQL statements are not allowed"):
        validate_read_only_sql("SELECT 1; SELECT 2")
