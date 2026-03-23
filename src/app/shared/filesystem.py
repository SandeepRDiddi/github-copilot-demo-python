from pathlib import Path


def resolve_within_root(root: Path, relative_path: str) -> Path:
    candidate = (root / relative_path).resolve()
    root_resolved = root.resolve()

    if candidate != root_resolved and root_resolved not in candidate.parents:
        raise ValueError(f"path '{relative_path}' is outside the configured workspace root")

    return candidate


def ensure_text_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"{path} does not exist")
    if not path.is_file():
        raise IsADirectoryError(f"{path} is not a file")
