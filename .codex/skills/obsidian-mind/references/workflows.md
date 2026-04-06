# Obsidian Mind Workflows

Use this skill when Codex is working in a vault that follows the Obsidian Mind Codex template.

## Pick the Right Playbook

| Need | Open |
|------|------|
| Kick off a session | `.codex/commands/standup.md` |
| Route a freeform dump | `.codex/commands/dump.md` |
| Close a session cleanly | `.codex/commands/wrap-up.md` |
| Synthesize the last week | `.codex/commands/weekly.md` |
| Audit vault quality | `.codex/commands/vault-audit.md` |
| Prepare reviews | `.codex/commands/review-brief.md`, `.codex/commands/self-review.md`, `.codex/commands/review-peer.md` |
| Capture a 1:1 or incident | `.codex/commands/capture-1on1.md`, `.codex/commands/incident-capture.md` |
| Archive or upgrade | `.codex/commands/project-archive.md`, `.codex/commands/vault-upgrade.md` |

## Core Rules

1. Read `AGENTS.md` before doing substantial work.
2. Put durable notes in the correct folder.
3. Use YAML frontmatter with `date`, `description`, and `tags`.
4. Add note-type-specific fields when required.
5. Give every durable note at least one `[[wikilink]]`.
6. Update the indexes when you add, move, or finish durable work.

## Helper Scripts

- `.codex/scripts/session-context.sh`: print a deterministic session summary
- `.codex/scripts/classify-message.py`: detect routing signals in raw text
- `.codex/scripts/validate-note.py`: check note hygiene after edits
- `.codex/scripts/charcount.sh`: verify character limits in review drafts
