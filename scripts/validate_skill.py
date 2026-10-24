#!/usr/bin/env python3
"""Validação básica, sem dependências externas, de Academic Research Architect."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "academic-research-architect"
REQUIRED = [
    SKILL / "SKILL.md",
    *(SKILL / "references" / item for item in (
        "academic-core.md", "structures.md", "editorial.md",
        "evidence.md", "methodology.md", "quality-review.md")),
    SKILL / "assets" / "configuration.md",
]
ERRORS = []


def fail(message):
    ERRORS.append(message)


for path in REQUIRED:
    if not path.is_file():
        fail(f"Ausente: {path.relative_to(ROOT)}")

if (SKILL / "SKILL.md").exists():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    sections = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not sections:
        fail("SKILL.md: frontmatter YAML ausente")
    else:
        front = sections.group(1)
        name = re.search(r"(?m)^name:\s*(.+)$", front)
        description = re.search(r"(?m)^description:\s*(.+)$", front)
        if not name or name.group(1).strip() != SKILL.name:
            fail("SKILL.md: nome deve corresponder à pasta")
        if not re.fullmatch(r"[a-z0-9-]{1,64}", SKILL.name):
            fail("Nome da pasta: requer kebab-case")
        if not description or not description.group(1).strip():
            fail("SKILL.md: description obrigatória")
        elif len(description.group(1).strip()) > 200:
            fail("SKILL.md: description excede 200 caracteres (limite conservador)")
    for target in re.findall(r"\]\((references/[^)]+|assets/[^)]+)\)", text):
        if not (SKILL / target).is_file():
            fail(f"Referência interna ausente: {target}")
    if (SKILL / "README.md").exists():
        fail("Não inclua README.md dentro da pasta instalável")

for path in SKILL.rglob("*") if SKILL.exists() else []:
    if path.is_symlink():
        fail(f"Symlink não permitido no ZIP: {path}")
    if path.is_file() and path.suffix in (".md", ".csv"):
        try:
            path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            fail(f"Arquivo não UTF-8: {path}")

if ERRORS:
    print("FALHA na validação:\n" + "\n".join(f"- {e}" for e in ERRORS))
    sys.exit(1)
print("OK: estrutura, YAML básico, referências e UTF-8.")

