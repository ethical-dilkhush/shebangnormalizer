"""CLI entry point for shebangnormalizer."""


import argparse
import os
import sys
from typing import Iterable

from shebangnormalizer.core import normalize_file
from shebangnormalizer.reporter import render_reports

DEFAULT_TARGET = "#!/usr/bin/env python3"
DEFAULT_INCLUDE = (".py", ".pyw", ".sh", "")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="shebangnormalizer",
        description="Normalize shebangs to a portable `python3` form.",
    )
    parser.add_argument("paths", nargs="*", default=["."])
    parser.add_argument("--target", default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--include", action="append", default=None)
    parser.add_argument("--reporter", default="text", choices=["text", "json"])
    parser.add_argument("--verbose", action="store_true")
    args = parser.parse_args(argv)

    target = args.target or DEFAULT_TARGET
    include = tuple(args.include or DEFAULT_INCLUDE)
    reports = []

    for path in args.paths:
        if os.path.isdir(path):
            reports.extend(normalize_tree(path, target=target, include=include, dry_run=args.dry_run))
        else:
            report = normalize_file(path, target=target, dry_run=args.dry_run)
            if report and report.normalized and _path_matches(path, include):
                reports.append(report)

    print(render_reports(reports, fmt=args.reporter))
    return 0


def _path_matches(path: str, include: tuple[str, ...]) -> bool:
    lowered = path.lower()
    suffixes = tuple(item.lower().lstrip(".") for item in include)
    if not suffixes:
        return True
    return lowered.endswith(suffixes) or lowered.startswith(suffixes)


if __name__ == "__main__":
    raise SystemExit(main())
