"""Project entrypoint.

This module stays intentionally tiny in early stages. It exists to validate that:
- configuration files are present
- the project is importable as a package tree
"""


def main() -> int:
    """Run the application.

    Returns:
        Process exit code.
    """

    print("MODULAR-RAG-MCP-SERVER: bootstrap OK (WIP)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
