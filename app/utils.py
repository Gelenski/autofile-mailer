from pathlib import Path

def is_extension_valid(file_path: Path) -> bool:
    return file_path.suffix.lower() in [".pdf"]

def extract_client(file_path: Path) -> str:
    return file_path.parent.name