from app.integrations.github.client import GitHubClient


def register_tools(mcp: object, client: GitHubClient) -> list[str]:
    @mcp.tool(name="github_list_repositories")
    def github_list_repositories(username: str) -> dict[str, object]:
        """List up to five GitHub repositories for a given user."""
        return {
            "username": username,
            "repositories": client.list_repositories(username),
        }

    return ["github_list_repositories"]
