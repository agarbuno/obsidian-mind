# Contributing

## Template Development Checklist

When adding or modifying Codex playbooks, scripts, or vault structure, keep these files in sync:

| File | What to update |
|------|---------------|
| `AGENTS.md` | Vault rules, workflow references, allowed root files, session lifecycle |
| `README.md` | Quick start, commands/playbooks tables, compatibility notes |
| `brain/Skills.md` | Playbook tables, helper scripts, usage notes, workflow examples |
| `.codex/commands/README.md` | Command playbook index |
| `.codex/playbooks/README.md` | Deep-work playbook index |
| `CHANGELOG.md` | New version entry at top with Added/Changed/Fixed sections |
| `vault-manifest.json` | Version number, infrastructure globs, scaffold paths, frontmatter schemas, version fingerprints |
| `bases/*.base` | If new properties or note types are added, update relevant Base views |

## Before Shipping the Template

- New playbooks appear in the command or playbook index files
- Any renamed file paths are reflected in `AGENTS.md`, `README.md`, `brain/Skills.md`, and the
  manifest
- `vault-manifest.json` version is bumped
- CHANGELOG has the new version entry
- All infrastructure paths in the manifest actually exist (`ls` each non-glob path)
- Examples use generic dates and names, not specific to any company or person
