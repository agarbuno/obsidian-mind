# Codex Command Playbooks

These files are manual prompt playbooks.

Codex does not auto-register repo-local workflow files, so use them explicitly:

- Ask Codex to "follow `.codex/commands/standup.md`"
- Ask Codex to "use the workflow in `.codex/commands/dump.md`"
- Paste the relevant file into the conversation if you want to modify the workflow

If a playbook still mentions an older command name or a delegated helper, interpret it as:

- a named workflow to follow manually
- an optional deeper analysis step, not automatic behavior
- something that should only be delegated when the Codex environment and user request allow it

## Common Playbooks

| File | Use it for |
|------|------------|
| `standup.md` | Session kickoff and orientation |
| `dump.md` | Freeform capture and routing |
| `wrap-up.md` | End-of-session review |
| `weekly.md` | Weekly synthesis |
| `humanize.md` | Editing text to sound like the user |
| `capture-1on1.md` | Turning a 1:1 transcript into a durable note |
| `incident-capture.md` | Capturing an incident into structured notes |
| `review-brief.md` | Building a manager or peer review brief |
| `self-review.md` | Drafting a self-review |
| `review-peer.md` | Drafting a peer review |
| `vault-audit.md` | Auditing the vault for hygiene problems |
| `vault-upgrade.md` | Migrating content from another vault |
| `project-archive.md` | Moving completed work into the archive |
