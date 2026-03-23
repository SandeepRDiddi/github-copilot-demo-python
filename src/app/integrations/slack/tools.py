from app.integrations.slack.client import SlackClient


def register_tools(mcp: object, client: SlackClient) -> list[str]:
    @mcp.tool(name="slack_post_message")
    def slack_post_message(channel: str, text: str) -> dict[str, object]:
        """Post a message to a Slack channel."""
        return client.post_message(channel=channel, text=text)

    return ["slack_post_message"]
