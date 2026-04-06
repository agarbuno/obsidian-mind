# Changelog

## v1.0.0 — 2026-04-05

Initial Codex edition of the vault, based on the Claude-compatible reference template in
`../reference/`.

### Added

- `AGENTS.md` as the Codex-native vault instruction file
- `.codex/commands/` manual prompt playbooks copied from the Claude command set
- `.codex/playbooks/` focused workflow specs adapted from the Claude subagents
- `.codex/scripts/session-context.sh` for explicit session kickoff
- `.codex/scripts/classify-message.py` for routing freeform input into note workflows
- `.codex/scripts/validate-note.py` for note hygiene checks
- `.codex/skills/obsidian-mind/` as an optional installable Codex skill bundle

### Changed

- `README.md` rewritten for Codex usage instead of Claude usage
- `brain/Skills.md` rewritten around playbooks, helper scripts, and explicit workflows
- `CONTRIBUTING.md` updated for the Codex file set
- `vault-manifest.json` updated to track Codex infrastructure instead of Claude infrastructure
