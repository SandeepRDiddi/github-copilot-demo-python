import httpx


def build_http_client(*, bearer_token: str | None = None, base_url: str | None = None) -> httpx.Client:
    headers = {}
    if bearer_token:
        headers["Authorization"] = f"Bearer {bearer_token}"

    return httpx.Client(
        base_url=base_url or "",
        headers=headers,
        timeout=20.0,
    )
