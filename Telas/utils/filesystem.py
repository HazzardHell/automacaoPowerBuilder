import os
import re

def safe_name(name: str) -> str:
    """Remove caracteres inválidos para nomes de pastas."""
    return re.sub(r'[<>:"/\\|?*]', '_', name)

def criar_pasta(base_path: str, name: str) -> str:
    path = os.path.join(base_path, safe_name(name))
    os.makedirs(path, exist_ok=True)
    return path
