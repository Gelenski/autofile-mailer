from pathlib import Path
import re

def is_extension_valid(file_path: Path) -> bool:
    return file_path.suffix.lower() in [".pdf"]

def extract_client(file_path: Path) -> str:
    return file_path.parent.name

def extract_file_number(file_path: Path) -> str | None:
    """
    Extract the file number from the file name.
    Using regular expressions, based on the pattern: Boleto_CLIENT_NUMBER.pdf.
    """
    match = re.search(r"Boleto_.*?_(\d+)\.pdf$", file_path.name)
    if match:
        return match.group(1)
    else:
        return None