# Obsidian Mind for Codex

[![Codex](https://img.shields.io/badge/codex-compatible-10A37F)](https://openai.com/codex/)
[![Obsidian](https://img.shields.io/badge/obsidian-1.12%2B-7C3AED)](https://obsidian.md)
[![Python](https://img.shields.io/badge/python-3.8%2B-3776AB)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

> An Obsidian vault that gives Codex durable working memory.

This is the Codex edition of the project stored in [`reference/`](../reference). The vault
structure stays the same, but the orchestration model changes:

- `AGENTS.md` replaces `CLAUDE.md`
- `.codex/commands/` replaces repo-local slash commands with explicit prompt playbooks
- `.codex/playbooks/` replaces repo-local Claude subagents with focused workflow specs
- `.codex/scripts/` replaces hooks with manual helper scripts
- `.codex/skills/obsidian-mind/` packages the workflow as an optional Codex skill bundle

## Quick Start

1. Open the `codex/` folder as an Obsidian vault.
2. Open the same folder in Codex.
3. Fill in `brain/North Star.md` with your goals.
4. Start a session with either:
   - `bash .codex/scripts/session-context.sh`
   - `Follow .codex/commands/standup.md for this vault.`
5. Capture updates with:
   - `Follow .codex/commands/dump.md and process this: ...`
6. End a session with:
   - `Follow .codex/commands/wrap-up.md.`

## Example Prompts

**Morning kickoff**

```text
Follow .codex/commands/standup.md for this vault.
```

**Brain dump after a meeting**

```text
Follow .codex/commands/dump.md and process this:

I just had a 1:1 with Sarah. She is happy with the auth work but wants
error monitoring before release. Tom also said the cache migration is now
deferred to Q2. Decision: defer Redis migration. Win: Sarah praised the
auth architecture.
```

**End of day**

```text
Follow .codex/commands/wrap-up.md for this session.
```

## Codex-Native Structure

| Path | Role in Codex |
|------|---------------|
| `AGENTS.md` | Repo instructions auto-read by Codex |
| `.codex/commands/` | Manual workflow playbooks for common vault tasks |
| `.codex/playbooks/` | Focused specs for deeper context loading, audits, and review prep |
| `.codex/scripts/` | Explicit utilities for context summaries, classification, note validation, and character limits |
| `.codex/skills/obsidian-mind/` | Optional installable skill bundle for Codex |

## Commands and Playbooks

### Command Playbooks

| File | Purpose |
|------|---------|
| `standup.md` | Morning kickoff and prioritization |
| `dump.md` | Freeform capture and routing |
| `wrap-up.md` | End-of-session review |
| `weekly.md` | Weekly synthesis |
| `humanize.md` | Voice-calibrated editing |
| `capture-1on1.md` | 1:1 note capture |
| `incident-capture.md` | Incident capture |
| `slack-scan.md` | Slack transcript or export scan |
| `peer-scan.md` | Peer PR scan |
| `review-brief.md` | Manager or peer review brief |
| `self-review.md` | Self-assessment drafting |
| `review-peer.md` | Peer review drafting |
| `vault-audit.md` | Vault hygiene audit |
| `vault-upgrade.md` | Vault migration and upgrade |
| `project-archive.md` | Archive completed work |

### Deep-Work Playbooks

| File | Purpose |
|------|---------|
| `context-loader.md` | Build a focused briefing on a person, project, incident, or concept |
| `cross-linker.md` | Find missing links and backlink gaps |
| `vault-librarian.md` | Audit note hygiene and stale notes |
| `brag-spotter.md` | Find uncaptured wins and competency evidence |
| `review-prep.md` | Aggregate evidence for a review period |
| `review-fact-checker.md` | Verify review claims against sources |
| `people-profiler.md` | Create or update person notes |
| `slack-archaeologist.md` | Reconstruct history from Slack material |
| `vault-migrator.md` | Classify and migrate notes from another vault |

## Helper Scripts

| Script | What it does |
|--------|---------------|
| `.codex/scripts/session-context.sh` | Prints North Star, recent changes, tasks, active work, and a vault file listing |
| `.codex/scripts/classify-message.py` | Detects routing hints in freeform text |
| `.codex/scripts/validate-note.py` | Checks frontmatter and wikilink hygiene |
| `.codex/scripts/charcount.sh` | Counts review section characters and enforces limits |

## Requirements

- [Obsidian](https://obsidian.md) 1.12+ for CLI support
- Codex
- Python 3
- Git
- [QMD](https://github.com/tobi/qmd) optional, for semantic search

## Compatibility Notes

- Codex does not currently auto-register repo-local slash commands or hooks from this project.
- The `.codex/` directory is intentionally explicit and transparent: you ask Codex to use a
  playbook or script when you want it.
- If your Codex environment supports delegated or parallel work, use the files in
  `.codex/playbooks/` as the specs for that work. Otherwise, Codex can still follow them directly
  in the main thread.

## Optional Skill Bundle

An installable skill bundle lives at `.codex/skills/obsidian-mind/`. It is useful if you want to
reuse these workflows across Codex sessions or copy the skill into `~/.codex/skills/`.

## Vault Principles

- Folders group by purpose; links group by meaning.
- A note without links is a bug.
- Durable knowledge belongs in the vault, not in chat memory.
- `thinking/` is a scratchpad, not long-term storage.
- Review prep should emerge from accumulated evidence, not last-minute reconstruction.
