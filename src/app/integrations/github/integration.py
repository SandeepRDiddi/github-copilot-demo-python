from app.integrations.github.client import GitHubClient
from app.integrations.github.tools import register_tools
from app.types import AppContext, IntegrationRegistration


class GitHubIntegration:
    name = "github"

    def register(self, mcp: object, context: AppContext) -> IntegrationRegistration:
        client = GitHubClient(token=context.settings.github_token)
        tool_names = register_tools(mcp, client)
        return IntegrationRegistration(
            name=self.name,
            enabled=True,
            tool_names=tool_names,
            metadata={"provider": "github"},
        )
