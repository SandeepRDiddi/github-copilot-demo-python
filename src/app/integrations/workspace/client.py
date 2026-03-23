from pathlib import Path

from app.shared.filesystem import ensure_text_file, resolve_within_root


class WorkspaceClient:
    def __init__(
        self,
        root: Path,
        *,
        exclude_hidden: bool = True,
        default_max_entries: int = 100,
        default_max_read_chars: int = 20000,
    ) -> None:
        self.root = root.resolve()
        self.exclude_hidden = exclude_hidden
        self.default_max_entries = default_max_entries
        self.default_max_read_chars = default_max_read_chars

    def list_files(self, relative_path: str = ".", max_entries: int = 100) -> list[dict[str, str]]:
        directory = resolve_within_root(self.root, relative_path)
        if not directory.exists():
            raise FileNotFoundError(f"{relative_path} does not exist")
        if not directory.is_dir():
            raise NotADirectoryError(f"{relative_path} is not a directory")

        max_entries = min(max_entries, self.default_max_entries)
        entries: list[dict[str, str]] = []
        for child in sorted(directory.iterdir(), key=lambda item: item.name.lower()):
            if self.exclude_hidden and child.name.startswith("."):
                continue

            child_relative = child.relative_to(self.root).as_posix()
            entries.append(
                {
                    "path": child_relative or ".",
                    "type": "directory" if child.is_dir() else "file",
                }
            )

            if len(entries) >= max_entries:
                break

        return entries

    def read_text_file(self, relative_path: str, max_chars: int = 20000) -> dict[str, str]:
        file_path = resolve_within_root(self.root, relative_path)
        ensure_text_file(file_path)

        max_chars = min(max_chars, self.default_max_read_chars)
        content = file_path.read_text(encoding="utf-8")
        truncated = content[:max_chars]
        return {
            "path": file_path.relative_to(self.root).as_posix(),
            "content": truncated,
            "truncated": len(content) > max_chars,
        }
