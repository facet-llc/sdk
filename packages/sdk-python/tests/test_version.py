"""Release-hygiene test: the packaged version and the newest dated
CHANGELOG section must agree.

Runs fully offline (no network, no ``smoke`` marker) so the default
``pytest`` invocation collects it. Paths are resolved relative to this
file so the test is independent of the working directory.
"""

from __future__ import annotations

import re
from pathlib import Path

PACKAGE_ROOT = Path(__file__).parents[1]
PYPROJECT = PACKAGE_ROOT / "pyproject.toml"
CHANGELOG = PACKAGE_ROOT / "CHANGELOG.md"

# Matches a dated release heading like: "## [0.2.0] - 2026-08-21".
# The undated "## [Unreleased]" heading is intentionally excluded.
_CHANGELOG_HEADING = re.compile(r"^## \[(\d+\.\d+\.\d+)\] - \d{4}-\d{2}-\d{2}", re.M)


def _pyproject_version() -> str:
    text = PYPROJECT.read_text(encoding="utf-8")
    try:
        import tomllib  # Python 3.11+
    except ModuleNotFoundError:
        # Fallback for 3.9/3.10: parse the version line directly.
        match = re.search(r'^version\s*=\s*"([^"]+)"', text, re.M)
        assert match is not None, "no version line found in pyproject.toml"
        return match.group(1)
    return tomllib.loads(text)["project"]["version"]


def _newest_changelog_version() -> str:
    text = CHANGELOG.read_text(encoding="utf-8")
    match = _CHANGELOG_HEADING.search(text)
    assert match is not None, "no dated release heading found in CHANGELOG.md"
    return match.group(1)


def test_pyproject_version_matches_changelog() -> None:
    pyproject_version = _pyproject_version()
    changelog_version = _newest_changelog_version()
    assert pyproject_version == changelog_version, (
        f"pyproject version {pyproject_version!r} does not match the newest "
        f"dated CHANGELOG version {changelog_version!r}"
    )
