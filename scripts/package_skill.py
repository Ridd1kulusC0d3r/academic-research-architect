#!/usr/bin/env python3
"""Cria ZIP instalável com a pasta da skill como raiz."""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import subprocess
import sys

root = Path(__file__).resolve().parent.parent
skill = root / "academic-research-architect"
destination = root / "dist" / "academic-research-architect.zip"
subprocess.run([sys.executable, str(root / "scripts" / "validate_skill.py")], check=True)
destination.parent.mkdir(parents=True, exist_ok=True)

files = sorted(
    p for p in skill.rglob("*")
    if p.is_file() and not any(part.startswith(".") for part in p.relative_to(skill).parts)
    and "__pycache__" not in p.parts
)
with ZipFile(destination, "w", ZIP_DEFLATED) as archive:
    for path in files:
        archive.write(path, path.relative_to(root).as_posix())

print(f"Pacote criado: {destination.relative_to(root)} ({len(files)} arquivos)")

