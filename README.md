[![Python](https://img.shields.io/badge/python-3.9%2B-blue?logo=python)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

# shebangnormalizer

Normalize script shebangs to a portable `#!/usr/bin/env python3` form.

## About

Shebang lines drift across machines, CI images, and shared environments. `shebangnormalizer` is a small CLI/library that rewrites interpreter headers to a standard, portable form. It is useful for anything you distribute, check into source control, or run across operating systems.

## Features

- Replaces hard-coded interpreter paths such as `#!/usr/bin/python3` with `#!/usr/bin/env python3`.
- Operates on single files or recursively walks directories.
- Preview changes with `--dry-run` before touching disk.
- Reports normalized files in plain text or JSON.
- Pure stdlib implementation with no third-party runtime dependencies.

## Installation

```bash
python -m pip install .
```

### Development install

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

## Development

```bash
PYTHONPATH=src python -m shebangnormalizer.cli .
PYTHONPATH=src python -m pytest tests -q
```
