READ_ONLY_PREFIXES = ("select", "with", "explain")
BLOCKED_SQL_TOKENS = (
    "insert ",
    "update ",
    "delete ",
    "drop ",
    "alter ",
    "create ",
    "truncate ",
    "grant ",
    "revoke ",
    "comment ",
    "copy ",
    "call ",
    "do ",
    "vacuum ",
    "refresh ",
)


def validate_read_only_sql(sql: str) -> str:
    normalized = " ".join(sql.strip().split())
    lowered = normalized.lower()

    if not normalized:
        raise ValueError("sql must not be empty")
    if lowered.startswith(READ_ONLY_PREFIXES) is False:
        raise ValueError("only SELECT, WITH, and EXPLAIN queries are allowed")
    if ";" in normalized.rstrip(";"):
        raise ValueError("multiple SQL statements are not allowed")

    padded = f" {lowered} "
    for token in BLOCKED_SQL_TOKENS:
        if token in padded:
            raise ValueError(f"blocked SQL token detected: {token.strip()}")

    return normalized
