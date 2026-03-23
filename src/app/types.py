from datetime import datetime, timezone
from dataclasses import dataclass
from typing import Any
from typing import Protocol

from app.config import Settings


@dataclass(slots=True)
class AppContext:
    settings: Settings
    started_at: datetime

    @classmethod
    def create(cls, settings: Settings) -> "AppContext":
        return cls(settings=settings, started_at=datetime.now(timezone.utc))


@dataclass(slots=True)
class IntegrationRegistration:
    name: str
    enabled: bool
    tool_names: list[str]
    metadata: dict[str, Any]


class Integration(Protocol):
    name: str

    def register(self, mcp: object, context: AppContext) -> IntegrationRegistration:
        """Register tools, resources, and prompts on the MCP server."""
