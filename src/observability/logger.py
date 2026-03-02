"""Observability logger (placeholder).

Stage A3 only requires a minimal logger helper so other modules can depend on it
without bringing a full logging stack.
"""

from __future__ import annotations

import logging


def get_logger(name: str) -> logging.Logger:
    """Get or create a logger.

    Args:
        name: Logger name.

    Returns:
        A configured logger emitting to stderr.
    """

    logger = logging.getLogger(name)
    if logger.handlers:
        return logger

    handler = logging.StreamHandler()
    formatter = logging.Formatter(
        fmt="%(asctime)s %(levelname)s %(name)s - %(message)s",
    )
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.INFO)
    return logger
