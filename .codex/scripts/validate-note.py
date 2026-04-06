#!/usr/bin/env python3
"""Validate vault note hygiene for one or more markdown files."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT_SKIP_FILES = {
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "AGENTS.md",
}


def should_skip(path: Path) -> bool:
    normalized = path.as_posix()
    basename = path.name

    if basename in ROOT_SKIP_FILES:
        return True
    if basename.startswith("README.") and basename.endswith(".md"):
        return True
    if any(part in normalized for part in ["/.codex/", "/.obsidian/", "/templates/", "/thinking/"]):
        return True
    return False


def validate(path: Path) -> list[str]:
    warnings: list[str] = []

    if path.suffix != ".md":
        return warnings
    if should_skip(path):
        return warnings

    try:
        content = path.read_text(encoding="utf-8")
    except OSError as exc:
        return [f"Could not read file: {exc}"]

    if not content.startswith("---"):
        warnings.append("Missing YAML frontmatter")
    else:
        parts = content.split("---", 2)
        if len(parts) >= 3:
            frontmatter = parts[1]
            for required in ["date:", "description:", "tags:"]:
                if required not in frontmatter and required.replace(":", " :") not in frontmatter:
                    warnings.append(f"Missing `{required[:-1]}` in frontmatter")
            normalized = path.as_posix()
            if "/work/active/" in normalized or "/work/archive/" in normalized:
                for required in ["status:", "quarter:"]:
                    if required not in frontmatter and required.replace(":", " :") not in frontmatter:
                        warnings.append(f"Missing `{required[:-1]}` for work note")
            if "/work/incidents/" in normalized:
                for required in ["status:", "quarter:", "ticket:", "severity:", "role:"]:
                    if required not in frontmatter and required.replace(":", " :") not in frontmatter:
                        warnings.append(f"Missing `{required[:-1]}` for incident note")
            if "/work/1-1/" in normalized:
                if "quarter:" not in frontmatter and "quarter :" not in frontmatter:
                    warnings.append("Missing `quarter` for 1:1 note")
            if "/org/people/" in normalized:
                if "title:" not in frontmatter and "title :" not in frontmatter:
                    warnings.append("Missing `title` for person note")

    if len(content) > 300 and "[[" not in content:
        warnings.append("No `[[wikilinks]]` found")

    return warnings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Obsidian Mind note hygiene.")
    parser.add_argument("paths", nargs="+", help="One or more markdown files to validate.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    has_warnings = False

    for raw_path in args.paths:
        path = Path(raw_path)
        warnings = validate(path)
        if warnings:
            has_warnings = True
            print(path)
            for warning in warnings:
                print(f"  - {warning}")

    if not has_warnings:
        print("All checked notes passed the configured hygiene checks.")
        return 0

    return 1


if __name__ == "__main__":
    raise SystemExit(main())
