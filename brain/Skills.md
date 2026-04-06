---
date: 2026-04-05
description: "Vault-specific Codex workflows, prompt playbooks, and helper scripts for review prep, project tracking, and vault maintenance"
tags:
  - brain
  - index
---

# Skills

Codex-facing workflows for this vault. The authoritative repo instructions live in `AGENTS.md`.
Use [[Home]] as the entry point and [[North Star]] to ground priorities before picking a workflow.

This Codex edition uses:

- `.codex/commands/` for manual prompt playbooks
- `.codex/playbooks/` for deeper focused workflows
- `.codex/scripts/` for explicit helper scripts
- `.codex/skills/obsidian-mind/` for an optional installable skill bundle

## Prompt Playbooks

### Daily Workflow

| Playbook | Purpose |
|---------|---------|
| `standup.md` | Morning kickoff — load context, review yesterday, surface tasks, identify priorities |
| `dump.md` | Freeform capture — route raw updates into the right notes |
| `wrap-up.md` | Full session review — verify notes, indexes, links, and suggest improvements |

### Editing & Synthesis

| Playbook | Purpose |
|---------|---------|
| `humanize.md` | Voice-calibrated editing — makes Codex-drafted text sound like you wrote it |
| `weekly.md` | Weekly synthesis — cross-session patterns, North Star alignment, uncaptured wins |

### Capture & Documentation

| Playbook | Purpose |
|---------|---------|
| `capture-1on1.md` | Capture a 1:1 transcript into a structured vault note |
| `incident-capture.md` | Capture incident context into structured notes |
| `slack-scan.md` | Deep scan Slack transcripts or exports for evidence |

### Performance & Review

| Playbook | Purpose |
|---------|---------|
| `peer-scan.md` | Deep scan a peer's GitHub PRs for review prep |
| `review-brief.md` | Generate review brief (manager or peer version) from vault data |
| `self-review.md` | Write a self-assessment from vault evidence |
| `review-peer.md` | Write a peer review from vault evidence |

### Vault Maintenance

| Playbook | Purpose |
|---------|---------|
| `vault-audit.md` | Deep structural audit — indexes, frontmatter, links, Bases, folder placement, stale context |
| `vault-upgrade.md` | Import content from an existing vault — detect version, classify notes, transform frontmatter, rebuild indexes |
| `project-archive.md` | Move completed project from `work/active/` to `work/archive/YYYY/`, update indexes |

## Usage Notes

**Daily:**
- `standup.md` replaces the blank-slate session start
- `dump.md` processes freeform text and routes each piece to the correct note type and folder
- `wrap-up.md` is a manual closeout workflow, not an automatic hook

**Editing & Synthesis:**
- `humanize.md` calibrates against actual writing samples, not a word blacklist
- `weekly.md` bridges standup and review prep with a cross-session synthesis

**Capture:**
- `capture-1on1.md` handles transcripts, raw notes, or summaries
- `incident-capture.md` handles Slack transcripts, exports, or manual notes
- `slack-scan.md` is most useful after `peer-scan.md` or before review prep

**Performance:**
- `peer-scan.md` works best when the user explicitly asks for deeper or parallel review prep
- `review-brief.md` can produce a manager or peer-oriented brief

**Maintenance:**
- `vault-audit.md` catches stale indexes, missing links, and mixed context
- `vault-upgrade.md` imports content from an older Obsidian Mind vault or any general Obsidian vault
- `project-archive.md` handles the active to archive move with index updates

## Deep-Work Playbooks

| Playbook | Purpose | Typical Trigger |
|-------|---------|------------|
| `brag-spotter.md` | Find uncaptured wins and competency gaps | `weekly.md`, `wrap-up.md` |
| `context-loader.md` | Load all vault context about a person, project, incident, or concept | "Load context on X" |
| `cross-linker.md` | Find missing wikilinks, orphans, and broken backlinks | `vault-audit.md` |
| `people-profiler.md` | Create or update person notes from source material | `incident-capture.md` |
| `review-prep.md` | Aggregate performance evidence for a review period | `review-brief.md` |
| `slack-archaeologist.md` | Reconstruct context from Slack transcripts or exports | `incident-capture.md` |
| `vault-librarian.md` | Audit note hygiene and stale notes | `vault-audit.md` |
| `review-fact-checker.md` | Verify review claims against vault sources | `self-review.md`, `review-peer.md` |
| `vault-migrator.md` | Classify and migrate content from a source vault | `vault-upgrade.md` |

These are instructions, not auto-registered repo-local agents.

## Helper Scripts

| Script | Purpose |
|------|------|
| `.codex/scripts/session-context.sh` | Print a session kickoff summary |
| `.codex/scripts/classify-message.py` | Detect routing hints in freeform input |
| `.codex/scripts/validate-note.py` | Validate note hygiene after edits |
| `.codex/scripts/charcount.sh` | Count review section characters and enforce limits |

## Semantic Search (QMD)

If QMD is installed (`npm install -g @tobilu/qmd`), the vault has semantic search:

- `qmd query "..."` — hybrid BM25 + vector + LLM reranking
- `qmd search "..."` — fast BM25 keyword search
- `qmd vsearch "..."` — semantic vector search
- `qmd update && qmd embed` — refresh the index after bulk changes

`.codex/scripts/session-context.sh` runs `qmd update` opportunistically. If you bulk-edit the vault,
run `qmd update && qmd embed` yourself.

## Workflow: Weekly Review

1. **`weekly.md`** — synthesize the week's activity, check alignment, find patterns
2. Promote any uncaptured wins to brag doc
3. Update North Star if focus shifted
4. **`wrap-up.md`** — close the session cleanly

## Workflow: Full Review Cycle Prep

1. **`review-brief.md`** — generate the manager or peer context transfer doc
2. **`peer-scan.md`** — deep scan peers' PRs
3. **`slack-scan.md`** — scan relevant transcripts or exports for context
4. **`capture-1on1.md`** — capture the review 1:1 with your manager
5. **`vault-audit.md`** — tidy up after all the new data

## Workflow: Project Ramp-Up

1. **`slack-scan.md`** — scan project channels or transcripts for history and decisions
2. **`peer-scan.md`** (if needed) — understand what teammates have already built
3. Create work note from gathered context
4. **`vault-audit.md`** — ensure everything links properly
