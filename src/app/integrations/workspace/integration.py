from app.integrations.workspace.client import WorkspaceClient
from app.integrations.workspace.tools import register_tools
from app.types import AppContext, IntegrationRegistration


class WorkspaceIntegration:
    name = "workspace"

    def register(self, mcp: object, context: AppContext) -> IntegrationRegistration:
        client = WorkspaceClient(
            root=context.settings.workspace_root,
            exclude_hidden=context.settings.workspace_exclude_hidden,
            default_max_entries=context.settings.workspace_max_entries,
            default_max_read_chars=context.settings.workspace_max_read_chars,
        )
        tool_names = register_tools(mcp, client)
        return IntegrationRegistration(
            name=self.name,
            enabled=True,
            tool_names=tool_names,
            metadata={
                "root": context.settings.workspace_root.as_posix(),
                "exclude_hidden": context.settings.workspace_exclude_hidden,
            },
        )
