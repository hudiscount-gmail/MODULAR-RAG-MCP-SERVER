"""Project entrypoint.

At stage A3 we start loading configuration from `config/settings.yaml`.
"""

from __future__ import annotations

import sys
from pathlib import Path


_REPO_ROOT = Path(__file__).resolve().parent
_SRC = _REPO_ROOT / "src"
if str(_SRC) not in sys.path:
    sys.path.insert(0, str(_SRC))


from core.settings import load_settings



def main() -> int:
    """Run the application.

    Returns:
        Process exit code.
    """
    settings = load_settings("config/settings.yaml")
    print(f"MODULAR-RAG-MCP-SERVER: bootstrap OK (app={settings.app.name})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
