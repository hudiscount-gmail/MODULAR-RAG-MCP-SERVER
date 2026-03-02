"""Smoke tests for package importability."""


def test_import_key_packages() -> None:
    """Key top-level packages should be importable.

    This ensures our skeleton directory tree is wired correctly.
    """

    import core  # noqa: F401
    import ingestion  # noqa: F401
    import libs  # noqa: F401
    import mcp_server  # noqa: F401
    import observability  # noqa: F401
