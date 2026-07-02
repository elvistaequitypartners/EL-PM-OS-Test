"""
Scan team and org memory for files that haven't been refreshed within
THRESHOLD_DAYS. For each stale file, open a GitHub issue routed to its owner.

Run by .github/workflows/staleness.yml on a weekly cron.
"""

from __future__ import annotations

import datetime as dt
import glob
import os
import subprocess
import sys
from pathlib import Path

import yaml


THRESHOLD_DAYS = int(os.environ.get("THRESHOLD_DAYS", "30"))
TODAY = dt.date.today()


def load_last_updated(path: str) -> tuple[dt.date | None, str | None]:
    """Return (last_updated, owner_email) parsed from YAML or MD frontmatter."""
    try:
        text = Path(path).read_text()
    except OSError:
        return None, None

    if path.endswith(".yaml"):
        try:
            doc = yaml.safe_load(text) or {}
        except yaml.YAMLError:
            return None, None
    else:
        # markdown with optional YAML frontmatter
        if not text.startswith("---"):
            return None, None
        try:
            _, front, _ = text.split("---", 2)
            doc = yaml.safe_load(front) or {}
        except (ValueError, yaml.YAMLError):
            return None, None

    raw = doc.get("last_updated")
    if not raw:
        return None, doc.get("owner")
    try:
        return dt.date.fromisoformat(str(raw)), doc.get("owner")
    except ValueError:
        return None, doc.get("owner")


def find_stale() -> list[tuple[str, int, str | None]]:
    paths = (
        glob.glob("memory/team/**/*.yaml", recursive=True)
        + glob.glob("memory/team/**/*.md", recursive=True)
        + glob.glob("memory/org/**/*.md", recursive=True)
    )
    stale: list[tuple[str, int, str | None]] = []
    for p in paths:
        last, owner = load_last_updated(p)
        if last is None:
            continue
        age = (TODAY - last).days
        if age > THRESHOLD_DAYS:
            stale.append((p, age, owner))
    return stale


def open_issue(path: str, age: int, owner: str | None) -> None:
    title = f"[staleness] {path} not updated in {age}d"
    body = (
        f"`{path}` was last updated {age} days ago (threshold: "
        f"{THRESHOLD_DAYS}). Owner: {owner or 'unassigned'}. "
        "Refresh `last_updated` or archive the file."
    )
    args = [
        "gh", "issue", "create",
        "--title", title,
        "--body", body,
        "--label", "staleness",
    ]
    if owner and "@" in owner:
        args += ["--assignee", owner.split("@")[0]]
    print("opening issue:", title)
    subprocess.run(args, check=False)


def main() -> int:
    stale = find_stale()
    if not stale:
        print(f"no files stale beyond {THRESHOLD_DAYS} days")
        return 0
    for path, age, owner in stale:
        open_issue(path, age, owner)
    return 0


if __name__ == "__main__":
    sys.exit(main())
