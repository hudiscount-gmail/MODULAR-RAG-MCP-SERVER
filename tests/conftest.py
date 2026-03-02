"""Pytest configuration.

We keep sources under `src/` but don't install the package yet in early stages.
This hook makes `import core`-style imports work for tests.
"""

from __future__ import annotations

import sys
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parent.parent
_SRC = _REPO_ROOT / "src"

if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))
