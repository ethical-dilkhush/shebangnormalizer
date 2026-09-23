"""Reporter helpers for shebangnormalizer."""

from __future__ import annotations

import json
from typing import Iterable

from shebangnormalizer.core import Report

TEXT_REPORTER = "{path} -> {updated}"


def render_reports(reports: Iterable[Report], fmt: str = "text") -> str:
    if fmt == "json":
        return json.dumps([report.__dict__ for report in reports], indent=2)
    return "\n".join(TEXT_REPORTER.format(**report.__dict__) for report in reports)
