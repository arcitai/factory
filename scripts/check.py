#!/usr/bin/env python3
"""Check this package's flat skill metadata and portable local Markdown links."""

from pathlib import Path
import re
import sys
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


def check(root=ROOT):
    root = Path(root).resolve()
    errors = []
    skills = [p for group in ("foundation", "agent-ops", "adlc")
              for p in (root / group).glob("*/SKILL.md")]
    if not skills:
        errors.append("No skills found")
    names = set()
    for path in skills:
        text = path.read_text(encoding="utf-8")
        parts = text.split("---", 2)
        if len(parts) != 3 or parts[0].strip():
            errors.append(f"{path.relative_to(root)}: missing frontmatter")
            continue
        fields = {}
        # The package deliberately uses only these three unquoted scalar keys.
        for line in parts[1].strip().splitlines():
            key, separator, value = line.partition(": ")
            if not separator or key not in {"name", "description", "license"} or key in fields:
                errors.append(f"{path.relative_to(root)}: unsupported/duplicate metadata")
                continue
            if not value or ": " in value or " #" in value or value[0] in "[{&*!|>'\"%@`":
                errors.append(f"{path.relative_to(root)}: use a plain one-line scalar")
            fields[key] = value
        name = fields.get("name", "")
        if (name != path.parent.name or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name)
                or len(name) > 64 or name in names):
            errors.append(f"{path.relative_to(root)}: invalid/duplicate name")
        names.add(name)
        if not 1 <= len(fields.get("description", "")) <= 1024 or fields.get("license") != "MIT":
            errors.append(f"{path.relative_to(root)}: description/license invalid")
    for path in root.rglob("*.md"):
        if any(part in {".git", "dist", ".venv"} for part in path.relative_to(root).parts):
            continue
        text = re.sub(r"```.*?```", "", path.read_text(encoding="utf-8"), flags=re.S)
        skill_root = next((p.parent for p in skills if path.is_relative_to(p.parent)), None)
        for raw in re.findall(r"\]\(([^)]+)\)", text):
            url = urlsplit(raw)
            if url.scheme or not url.path:
                continue
            target = (path.parent / unquote(url.path)).resolve()
            if not target.exists():
                errors.append(f"{path.relative_to(root)}: broken link {raw}")
            if skill_root and not target.is_relative_to(skill_root.resolve()):
                errors.append(f"{path.relative_to(root)}: skill link escapes its staged folder: {raw}")
    return errors, len(skills)


if __name__ == "__main__":
    errors, count = check()
    for error in errors:
        print(error, file=sys.stderr)
    print(f"{count} skills checked; {len(errors)} errors")
    sys.exit(bool(errors))
