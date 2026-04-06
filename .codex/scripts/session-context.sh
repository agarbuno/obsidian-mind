#!/usr/bin/env bash
set -euo pipefail

ROOT="${1:-.}"
cd "$ROOT"

run_with_timeout() {
  local timeout_sec=$1
  shift
  local fallback_cmd=$1
  shift

  if command -v gtimeout >/dev/null 2>&1; then
    gtimeout "$timeout_sec" "$@" 2>/dev/null || eval "$fallback_cmd"
  elif command -v timeout >/dev/null 2>&1; then
    timeout "$timeout_sec" "$@" 2>/dev/null || eval "$fallback_cmd"
  else
    "$@" 2>/dev/null || eval "$fallback_cmd"
  fi
}

qmd update 2>/dev/null || true

echo "## Session Context"
echo
echo "### Date"
date "+%Y-%m-%d (%A)"
echo

echo "### North Star (current goals)"
if command -v obsidian >/dev/null 2>&1; then
  run_with_timeout 5 'cat brain/North\ Star.md 2>/dev/null | head -30 || echo "(not found)"' \
    obsidian read file="North Star" | head -30
else
  cat brain/North\ Star.md 2>/dev/null | head -30 || echo "(not found)"
fi
echo

echo "### Recent Changes (last 48h)"
if git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  git log --oneline --since="48 hours ago" --no-merges 2>/dev/null | head -15 || echo "(no git history)"
else
  echo "(no git history)"
fi
echo

echo "### Open Tasks"
if command -v obsidian >/dev/null 2>&1; then
  run_with_timeout 5 'echo "(CLI timed out)"' obsidian tasks daily todo | head -10
else
  echo "(Obsidian CLI not available)"
fi
echo

echo "### Active Work"
active_work="$(find work/active -maxdepth 1 -type f -name '*.md' 2>/dev/null | sort | sed 's|^work/active/||; s|\.md$||' | head -10)"
if [ -n "$active_work" ]; then
  printf '%s\n' "$active_work"
else
  echo "(none)"
fi
echo

echo "### Vault File Listing"
find . -name "*.md" \
  -not -path "./.git/*" \
  -not -path "./.obsidian/*" \
  -not -path "./thinking/*" \
  -not -path "./.codex/*" \
  | sort
