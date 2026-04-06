# Obsidian Mind for Codex

This repository is an Obsidian vault that acts as a durable working memory for projects, people,
decisions, incidents, and review evidence.

## Codex Model

- `AGENTS.md` is the authoritative Codex instruction file for this vault.
- `.codex/commands/` contains manual prompt playbooks for common vault workflows.
- `.codex/playbooks/` contains deeper, scoped workflows for focused tasks.
- `.codex/scripts/` contains explicit helper scripts for classification, validation, and context loading.
- `.codex/skills/obsidian-mind/` contains an optional installable skill bundle for Codex.

Do not assume repo-local commands, playbooks, or scripts run automatically. Use them explicitly.

## Preferred Tooling

- Prefer Obsidian CLI when it is available. It is vault-aware and works better than raw filesystem
  operations for search, backlinks, tags, and tasks.
- Prefer QMD when it is installed for semantic search:
  - `qmd query "..."` for hybrid retrieval
  - `qmd search "..."` for keyword search
  - `qmd vsearch "..."` for semantic search
- Fall back to `rg`, `find`, and direct file reads when QMD or Obsidian CLI are unavailable.

## Vault Structure

| Path | Purpose |
|------|---------|
| `Home.md` | Vault entry point and dashboard |
| `vault-manifest.json` | Template metadata, required fields, upgrade fingerprints |
| `bases/` | Obsidian Bases used for dashboards and navigation |
| `work/active/` | Current projects only |
| `work/archive/YYYY/` | Completed work grouped by year |
| `work/incidents/` | Incident notes and follow-ups |
| `work/1-1/` | 1:1 meeting notes |
| `perf/` | Brag doc, evidence, competencies, and review-cycle notes |
| `brain/` | Durable operating knowledge for the vault |
| `org/` | People and team context |
| `reference/` | Codebase, architecture, and topic notes |
| `thinking/` | Scratchpads and temporary analysis |
| `templates/` | Note templates |
| `.codex/commands/` | Manual Codex prompt playbooks |
| `.codex/playbooks/` | Deeper scoped workflows |
| `.codex/scripts/` | Helper scripts for context, classification, validation |

## Starting a Substantial Session

Use one of these two paths:

1. Run `.codex/scripts/session-context.sh`
2. Follow `.codex/commands/standup.md`

If you need to do it manually:

1. Read `Home.md`
2. Read `brain/North Star.md`
3. Check `work/Index.md`
4. Scan `brain/Memories.md`, then read any relevant topic notes
5. Check `obsidian tasks daily todo` if the Obsidian CLI is available

## Ending a Substantial Session

When the user asks to wrap up, follow `.codex/commands/wrap-up.md`.

If you are ending a session without that playbook, at minimum:

1. Archive completed work from `work/active/` to `work/archive/YYYY/`
2. Update `work/Index.md` if new notes, decisions, or status changes happened
3. Update the relevant `brain/` note if the session revealed durable decisions, patterns, or
   gotchas
4. Update `org/People & Context.md` if org context changed
5. Update `perf/Brag Doc.md` if the session produced wins or impact
6. Verify all durable notes link to at least one existing note

Skip steps that do not apply, but do not leave durable context stranded in the conversation.

## Obsidian CLI

When Obsidian is running, prefer:

```bash
obsidian read file="Note Name"
obsidian create name="Name" content="..." silent
obsidian append file="Name" content="..."
obsidian search query="text" limit=10
obsidian backlinks file="Name"
obsidian tasks daily todo
obsidian property:set name="status" value="done" file="Name"
obsidian orphans
```

Use `file=` for wikilink-like resolution and `path=` for exact paths from the vault root.

## Note Creation Rules

### Frontmatter

Every durable note should use YAML frontmatter with at least:

- `date`
- `description`
- `tags`

Additional required fields:

- Work notes: `status`, `quarter`
- Incidents: `status`, `quarter`, `ticket`, `severity`, `role`
- 1:1 notes: `quarter`
- People: `title`

Use the templates in `templates/` whenever they fit.

### Placement

- Active project work goes in `work/active/`
- Completed work goes in `work/archive/YYYY/`
- Incident documentation goes in `work/incidents/`
- 1:1 notes go in `work/1-1/`
- Performance evidence goes in `perf/`
- People go in `org/people/`
- Teams go in `org/teams/`
- Durable operating knowledge goes in `brain/`
- Codebase or architecture knowledge goes in `reference/`
- Scratch work goes in `thinking/`

Do not create user notes at the vault root.

### Naming

- Use descriptive note titles as filenames
- Keep active project filenames stable
- Name 1:1 notes `<Person> YYYY-MM-DD.md`
- Prefer one note per concept instead of a large mixed document

## Linking Rules

Graph-first organization is the core rule in this vault.

- Every durable note must link to at least one existing note
- Prefer `[[wikilinks]]` over markdown links within the vault
- Work notes should link to people, teams, decisions, and competencies where relevant
- Index notes should curate outbound links
- Concept notes should stay definitional and receive evidence through backlinks

If a note has three or more distinct concepts that could stand alone, split it.

## Indexes to Maintain

Update these when you add or move durable notes:

- `work/Index.md`
- `brain/Memories.md`
- `brain/Skills.md`
- `org/People & Context.md`
- `perf/Brag Doc.md`

## Thinking Workflow

Use `thinking/` for drafts, rough analysis, or synthesis before creating durable notes.

1. Create a scratch note in `thinking/`
2. Reason there freely
3. Promote durable findings into the proper vault locations
4. Delete the scratch note if it no longer serves a purpose

## Decision Records and Wins

- Use the Decision Record template for important calls
- Link decisions from the work notes that led to them
- Log important decisions in `work/Index.md`
- Add notable wins to `perf/Brag Doc.md` with links to evidence

## North Star

`brain/North Star.md` is a living document.

- Read it at the start of substantial sessions
- Reference it when prioritizing work or tradeoffs
- Suggest updates when the user's focus clearly shifts

## Tags Convention

Use frontmatter tags, not inline tags.

- Type tags: `work-note`, `decision`, `perf`, `thinking`, `north-star`, `competency`, `person`,
  `team`, `brain`
- Index tags: `index`, `moc`
- Status is usually a dedicated frontmatter field: `active`, `completed`, `archived`,
  `proposed`, `accepted`, `deprecated`

## Codex Compatibility Rules

- Do not assume repo-local command registration exists.
- When a user asks for a workflow such as standup, dump, weekly review, or wrap-up, open the
  matching file under `.codex/commands/` and follow it explicitly.
- Treat `.codex/playbooks/` as scoped instructions. If your Codex environment requires explicit
  user consent before delegation or parallel agent work, get that consent first.
- Use `.codex/scripts/validate-note.py <path>` after substantial note edits when it helps catch
  missing frontmatter or links.
- Use `.codex/scripts/classify-message.py` to triage large freeform dumps before routing them.

The goal is durable, well-linked vault state, not hidden automation.
