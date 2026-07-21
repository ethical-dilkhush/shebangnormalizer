"""Tests for shebangnormalizer."""

from __future__ import annotations

from pathlib import Path

from shebangnormalizer.cli import main
from shebangnormalizer.core import normalize_file, path_matches


def test_normalizes_python_shebang(tmp_path: Path):
    """A Python shebang should be replaced with the env form."""

    target = tmp_path / "script.py"
    target.write_text("#!/usr/bin/python3\nprint(1)\n", encoding="utf-8")
    rc = main([str(target), "--target", "#!/usr/bin/env python3"])
    assert rc == 0
    assert target.read_text(encoding="utf-8").splitlines()[0] == "#!/usr/bin/env python3"


def test_skips_non_python_file(tmp_path: Path):
    """A file without a Python shebang should be untouched."""

    target = tmp_path / "readme.txt"
    target.write_text("hello world\n", encoding="utf-8")
    rc = main([str(target), "--target", "#!/usr/bin/env python3"])
    assert rc == 0
    assert target.read_text(encoding="utf-8") == "hello world\n"


def test_dry_run_previews_without_writing(tmp_path: Path):
    """Dry run should report the file but leave it unchanged."""

    target = tmp_path / "script.py"
    target.write_text("#!/usr/bin/python3\n", encoding="utf-8")
    before = target.read_bytes()
    rc = main([str(target), "--target", "#!/usr/bin/env python3", "--dry-run"])
    assert rc == 0
    assert target.read_bytes() == before
