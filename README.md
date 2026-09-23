[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Tests](https://img.shields.io/badge/tests-passing-brightgreen.svg)](#development)

# shebangnormalizer

Normalize script shebangs to a portable `#!/usr/bin/env python3` form.

## About

Shebang lines drift across machines, CI images, and shared environments. `shebangnormalizer` is a small CLI/library that rewrites interpreter headers to a standard, portable form.

It focuses on Python scripts because that is the most common portability failure, but it can operate on any file whose first line begins with `python`.

## Features

- Replaces hard-coded interpreter paths such as `#!/usr/bin/python3` with `#!/usr/bin/env python3`.
- Operates on single files or recursively walks directories.
- Preview changes with `--dry-run` before touching disk.
- Output in plain text or JSON.
- Pure stdlib implementation with no third-party runtime dependencies.

## Installation

```bash
python -m pip install .
```

### Source install

```bash
git clone https://github.com/ethical-dilkhush/shebangnormalizer.git
cd shebangnormalizer
python -m pip install -e .
```

## Usage

```bash
shebangnormalizer .
shebangnormalizer ./scripts --target '#!/usr/bin/env python3'
shebangnormalizer main.py config.py --dry-run
shebangnormalizer ./scripts --reporter json
```

## Project structure

```
shebangnormalizer/
  src/shebangnormalizer/
    __init__.py
    __main__.py
    cli.py
    core.py
    reporter.py
  tests/
    test_shebangnormalizer.py
  pyproject.toml
  README.md
  LICENSE
  .gitignore
  .github/workflows/
    tests.yml
```

Source: [https://github.com/ethical-dilkhush/shebangnormalizer](https://github.com/ethical-dilkhush/shebangnormalizer)

## Development

```bash
PYTHONPATH=src python -m shebangnormalizer.cli .
PYTHONPATH=src python -m pytest tests -q
```

## License

[MIT](LICENSE)
