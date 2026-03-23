from app.integrations.workspace.client import WorkspaceClient


def register_tools(mcp: object, client: WorkspaceClient) -> list[str]:
    @mcp.tool(name="workspace_list_files")
    def workspace_list_files(path: str = ".", max_entries: int = 100) -> dict[str, object]:
        """List files and folders within the configured workspace root."""
        return {
            "root": client.root.as_posix(),
            "entries": client.list_files(relative_path=path, max_entries=max_entries),
        }

    @mcp.tool(name="workspace_read_text_file")
    def workspace_read_text_file(path: str, max_chars: int = 20000) -> dict[str, str]:
        """Read a UTF-8 text file within the configured workspace root."""
        return client.read_text_file(relative_path=path, max_chars=max_chars)

    return ["workspace_list_files", "workspace_read_text_file"]
