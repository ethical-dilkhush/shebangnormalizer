"""Normalization report and file-level helpers."""

from __future__ import annotations

import argparse
import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Optional


@dataclass(frozen=True)
class Report:
    path: str
    normalized: bool
    original: str = ""
    updated: str = ""


PYTHON_SHEBANG_PREFIXES = (
    "#!/usr/bin/python",
    "#!/usr/bin/env python",
)


def _looks_like_python_shebang(line: str) -> bool:
    return line.startswith(PYTHON_SHEBANG_PREFIXES)


def _load_text(path: str) -> Optional[tuple[str, bool]]:
    try:
        data = Path(path).read_bytes()
    except OSError:
        return None
    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None
    return text, True


def normalize_file(
    path: str,
    target: str = "#!/usr/bin/env python3",
    dry_run: bool = False,
) -> Optional[Report]:
    loaded = _load_text(path)
    if not loaded:
        return None
    text, _ = loaded
    if not text:
        return None

    lines = text.splitlines()
    if not lines:
        return None

    first = lines[0] if lines[0].startswith("#!") else ""
    if not first or not _looks_like_python_shebang(first):
        return None

    if first == target:
        return Report(path, normalized=False, original=first, updated=first)

    updated = target + text[len(first) :]

    if not dry_run:
        Path(path).write_text(updated, encoding="utf-8")

    return Report(path, normalized=True, original=first, updated=target)


def path_matches(path: str, include: Iterable[str]) -> bool:
    lowered = path.lower()
    include_items = tuple(item.lower().lstrip(".") for item in include)
    if not include_items:
        return True
    return lowered.endswith(include_items) or lowered.startswith(include_items)

