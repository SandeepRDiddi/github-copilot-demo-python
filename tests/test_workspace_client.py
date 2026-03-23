from pathlib import Path

import pytest

from app.integrations.workspace.client import WorkspaceClient


def test_workspace_list_files_skips_hidden_entries(tmp_path: Path) -> None:
    (tmp_path / ".secret").write_text("hidden", encoding="utf-8")
    (tmp_path / "visible.txt").write_text("visible", encoding="utf-8")

    client = WorkspaceClient(root=tmp_path, exclude_hidden=True)

    entries = client.list_files()

    assert entries == [{"path": "visible.txt", "type": "file"}]


def test_workspace_read_text_file_blocks_directory_escape(tmp_path: Path) -> None:
    client = WorkspaceClient(root=tmp_path)

    with pytest.raises(ValueError, match="outside the configured workspace root"):
        client.read_text_file("../outside.txt")
