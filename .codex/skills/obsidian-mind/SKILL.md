---
name: obsidian-mind
description: Operate an Obsidian Mind vault in Codex. Use when working in a repository that follows the Obsidian Mind structure with `brain/`, `work/`, `org/`, `perf/`, `reference/`, `AGENTS.md`, and `.codex/` workflow files. This skill is for session kickoff, freeform capture, wrap-up, weekly review, vault audits, review prep, and maintaining note hygiene with YAML frontmatter and wikilinks.
---

# Obsidian Mind

## Overview

Operate a vault-first work memory system inside Codex. Use explicit playbooks and helper scripts to
capture durable context in the right notes instead of relying on hidden automation.

## Workflow

1. Read `AGENTS.md` first when it exists at the repository root.
2. For standup, dump, wrap-up, weekly review, or migration tasks, open the matching file under
   `.codex/commands/`.
3. For a deeper focused workflow, open the matching file under `.codex/playbooks/`.
4. Prefer `.codex/scripts/session-context.sh` for a deterministic kickoff,
   `.codex/scripts/classify-message.py` for routing hints, and
   `.codex/scripts/validate-note.py` after writing durable notes.
5. Prefer Obsidian CLI and QMD when available. Fall back to the filesystem when they are not.

## Durable Note Rules

- Use YAML frontmatter with `date`, `description`, and `tags`.
- Add `status` and `quarter` for work notes, plus `ticket`, `severity`, and `role` for incidents.
- Place notes in the correct folder instead of using the vault root.
- Give every durable note at least one `[[wikilink]]` to an existing note.
- Update the relevant indexes after adding or moving durable notes.

## References

- Read `references/workflows.md` for playbook selection and core vault rules.
