import httpx

from app.shared.errors import IntegrationConfigurationError
from app.shared.http import build_http_client


class GitHubClient:
    def __init__(self, token: str | None) -> None:
        self._token = token

    def _client(self) -> httpx.Client:
        if not self._token:
            raise IntegrationConfigurationError(
                "GitHub integration is enabled but MCP_GITHUB_TOKEN is not set."
            )
        return build_http_client(
            bearer_token=self._token,
            base_url="https://api.github.com",
        )

    def list_repositories(self, username: str) -> list[dict[str, str]]:
        with self._client() as client:
            response = client.get(f"/users/{username}/repos", params={"per_page": 5})
            response.raise_for_status()

        repos = response.json()
        return [
            {
                "name": repo["name"],
                "url": repo["html_url"],
                "visibility": "private" if repo["private"] else "public",
            }
            for repo in repos
        ]
