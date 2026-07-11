#!/usr/bin/env python3
"""Validate publishable Markdown and Quarto notes without third-party packages."""

from __future__ import annotations

import re
import sys
from pathlib import Path


NOTES_DIR = Path(__file__).resolve().parents[1] / "notes"
EXCLUDED = {"index.qmd", "_note-template.qmd"}
REQUIRED_FIELDS = ("title", "description", "date", "categories")
FILENAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*\.(?:md|qmd)$")
DATE_PATTERN = re.compile(r"^['\"]?\d{4}-\d{2}-\d{2}['\"]?(?:\s+#.*)?$")


def front_matter(path: Path) -> dict[str, str]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("file must begin with a YAML front matter block (---)")

    try:
        end = next(i for i, line in enumerate(lines[1:], 1) if line.strip() == "---")
    except StopIteration as exc:
        raise ValueError("YAML front matter is missing its closing ---") from exc

    fields: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([A-Za-z][A-Za-z0-9_-]*):\s*(.*)$", line)
        if match:
            fields[match.group(1)] = match.group(2).strip()
    return fields


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    if not FILENAME_PATTERN.fullmatch(path.name):
        errors.append("filename must use lowercase letters, numbers, and single hyphens")

    try:
        fields = front_matter(path)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    for field in REQUIRED_FIELDS:
        if field not in fields or not fields[field]:
            errors.append(f"required front matter field '{field}' is missing or empty")

    if fields.get("date") and not DATE_PATTERN.fullmatch(fields["date"]):
        errors.append("date must use YYYY-MM-DD format")

    categories = fields.get("categories", "")
    if categories and not (categories.startswith("[") and categories.endswith("]")):
        errors.append("categories must use inline YAML list syntax, e.g. [geometric analysis]")

    return errors


def main() -> int:
    note_paths = sorted(
        path
        for pattern in ("*.md", "*.qmd")
        for path in NOTES_DIR.glob(pattern)
        if path.name not in EXCLUDED
    )
    failures = {path: validate(path) for path in note_paths}
    failures = {path: errors for path, errors in failures.items() if errors}

    if failures:
        print("Note validation failed:", file=sys.stderr)
        for path, errors in failures.items():
            for error in errors:
                print(f"  - {path.relative_to(NOTES_DIR.parent)}: {error}", file=sys.stderr)
        return 1

    print(f"Validated {len(note_paths)} published note(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
