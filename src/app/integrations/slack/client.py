import httpx

from app.shared.errors import IntegrationConfigurationError
from app.shared.http import build_http_client


class SlackClient:
    def __init__(self, bot_token: str | None) -> None:
        self._bot_token = bot_token

    def _client(self) -> httpx.Client:
        if not self._bot_token:
            raise IntegrationConfigurationError(
                "Slack integration is enabled but MCP_SLACK_BOT_TOKEN is not set."
            )
        return build_http_client(
            bearer_token=self._bot_token,
            base_url="https://slack.com/api",
        )

    def post_message(self, channel: str, text: str) -> dict[str, object]:
        with self._client() as client:
            response = client.post(
                "/chat.postMessage",
                json={"channel": channel, "text": text},
            )
            response.raise_for_status()

        payload = response.json()
        if not payload.get("ok"):
            raise RuntimeError(f"Slack API error: {payload.get('error', 'unknown_error')}")

        return {
            "channel": payload.get("channel", channel),
            "timestamp": payload.get("ts"),
            "message": payload.get("message", {}).get("text", text),
        }
