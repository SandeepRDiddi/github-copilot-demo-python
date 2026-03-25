from pathlib import Path

import pytest

from app.shared.filesystem import ensure_text_file, resolve_within_root


def test_resolve_within_root_returns_path_inside_root(tmp_path: Path) -> None:
    nested_file = tmp_path / "docs" / "notes.txt"
    nested_file.parent.mkdir()
    nested_file.write_text("hello", encoding="utf-8")

    resolved = resolve_within_root(tmp_path, "docs/notes.txt")

    assert resolved == nested_file.resolve()


def test_resolve_within_root_rejects_path_outside_root(tmp_path: Path) -> None:
    with pytest.raises(ValueError, match="outside the configured workspace root"):
        resolve_within_root(tmp_path, "../outside.txt")


def test_ensure_text_file_raises_for_missing_file(tmp_path: Path) -> None:
    missing_file = tmp_path / "missing.txt"

    with pytest.raises(FileNotFoundError, match="does not exist"):
        ensure_text_file(missing_file)


def test_ensure_text_file_raises_for_directory_path(tmp_path: Path) -> None:
    directory = tmp_path / "folder"
    directory.mkdir()

    with pytest.raises(IsADirectoryError, match="is not a file"):
        ensure_text_file(directory)
