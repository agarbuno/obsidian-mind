# Changelog

## v1.0.0 — 2026-04-05

Initial Codex edition of the vault, based on the reference template in
`../reference/`.

### Added

- `AGENTS.md` as the Codex-native vault instruction file
- `.codex/commands/` manual prompt playbooks for the main vault workflows
- `.codex/playbooks/` focused workflow specs for deeper tasks
- `.codex/scripts/session-context.sh` for explicit session kickoff
- `.codex/scripts/classify-message.py` for routing freeform input into note workflows
- `.codex/scripts/validate-note.py` for note hygiene checks
- `.codex/skills/obsidian-mind/` as an optional installable Codex skill bundle

### Changed

- `README.md` rewritten for Codex usage
- `brain/Skills.md` rewritten around playbooks, helper scripts, and explicit workflows
- `CONTRIBUTING.md` updated for the Codex file set
- `vault-manifest.json` updated to track Codex infrastructure
