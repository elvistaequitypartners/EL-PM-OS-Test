#!/usr/bin/env bash
# PM Operating System — SessionStart hook.
#
# Runs at the start of every Claude Code session:
#   1. Pull latest team memory from git (GitOps: continuously reconciled)
#   2. Resolve $CURRENT_TEAM from .pm-os.yaml so skills know which team scope to load
#
# Wired via .claude/settings.json > hooks.SessionStart

set -euo pipefail

REPO="${CLAUDE_PROJECT_DIR:-$(pwd)}"
cd "$REPO"

# 1. Pull latest — only if on a branch tracking a remote
if git symbolic-ref -q HEAD >/dev/null 2>&1 \
   && git rev-parse --abbrev-ref '@{u}' >/dev/null 2>&1; then
  if ! git fetch --quiet 2>/dev/null; then
    echo "PM-OS: git fetch failed (offline? auth?) — continuing with local state" >&2
  elif ! git pull --rebase --autostash --quiet 2>/dev/null; then
    echo "PM-OS: rebase failed — resolve manually before trusting team memory" >&2
  fi
fi

# 2. Resolve current team from .pm-os.yaml (falls back to $PM_TEAM env var)
if [ -z "${PM_TEAM:-}" ] && [ -f .pm-os.yaml ]; then
  CURRENT_TEAM=$(awk -F': *' '/^team:/ { print $2; exit }' .pm-os.yaml)
  if [ -n "$CURRENT_TEAM" ]; then
    export CURRENT_TEAM
    echo "PM-OS: team scope = $CURRENT_TEAM"
  fi
fi

exit 0
