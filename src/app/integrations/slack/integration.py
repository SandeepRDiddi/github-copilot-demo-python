from app.integrations.slack.client import SlackClient
from app.integrations.slack.tools import register_tools
from app.types import AppContext, IntegrationRegistration


class SlackIntegration:
    name = "slack"

    def register(self, mcp: object, context: AppContext) -> IntegrationRegistration:
        client = SlackClient(bot_token=context.settings.slack_bot_token)
        tool_names = register_tools(mcp, client)
        return IntegrationRegistration(
            name=self.name,
            enabled=True,
            tool_names=tool_names,
            metadata={"provider": "slack"},
        )
