"""Allow python -m shebangnormalizer to invoke the CLI."""

from __future__ import annotations

import sys

from shebangnormalizer.cli import main


def main_entry(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    return main(args)


if __name__ == "__main__":
    raise SystemExit(main_entry())
