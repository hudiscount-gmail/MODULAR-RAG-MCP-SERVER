"""Settings load/validation.

Only includes structure + minimal validation. It must not initialize external
clients (network/IO) at import time.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml


class SettingsError(ValueError):
    """Raised when settings are missing or invalid."""


@dataclass(frozen=True)
class AppSettings:
    """Application metadata settings."""

    name: str


@dataclass(frozen=True)
class ProviderSettings:
    """Generic provider settings with the minimal `provider` field."""

    provider: str


@dataclass(frozen=True)
class Settings:
    """Strongly typed settings root object."""

    app: AppSettings
    llm: ProviderSettings
    embedding: ProviderSettings
    vector_store: ProviderSettings
    retrieval: ProviderSettings
    rerank: ProviderSettings
    evaluation: ProviderSettings
    observability: ProviderSettings


def _require(d: dict[str, Any], path: str) -> Any:
    """Require a value from nested dict.

    Args:
        d: Root mapping.
        path: Dot-separated key path.

    Returns:
        The value.

    Raises:
        SettingsError: If missing.
    """

    cur: Any = d
    for key in path.split("."):
        if not isinstance(cur, dict) or key not in cur:
            raise SettingsError(f"Missing required setting: {path}")
        cur = cur[key]
    return cur


def validate_settings(settings: Settings) -> None:
    """Validate settings object.

    Args:
        settings: Parsed settings.

    Raises:
        SettingsError: If invalid.
    """

    if not settings.app.name.strip():
        raise SettingsError("Missing required setting: app.name")

    for field_name in (
        "llm",
        "embedding",
        "vector_store",
        "retrieval",
        "rerank",
        "evaluation",
        "observability",
    ):
        provider = getattr(settings, field_name).provider
        if not provider or not provider.strip():
            raise SettingsError(f"Missing required setting: {field_name}.provider")


def load_settings(path: str) -> Settings:
    """Load settings from a YAML file.

    Args:
        path: YAML path.

    Returns:
        Parsed settings.

    Raises:
        SettingsError: If missing/invalid.
    """

    p = Path(path)
    if not p.exists():
        raise SettingsError(f"Settings file not found: {path}")

    raw = yaml.safe_load(p.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise SettingsError("Settings YAML root must be a mapping")

    settings = Settings(
        app=AppSettings(name=str(_require(raw, "app.name"))),
        llm=ProviderSettings(provider=str(_require(raw, "llm.provider"))),
        embedding=ProviderSettings(provider=str(_require(raw, "embedding.provider"))),
        vector_store=ProviderSettings(provider=str(_require(raw, "vector_store.provider"))),
        retrieval=ProviderSettings(provider=str(_require(raw, "retrieval.provider"))),
        rerank=ProviderSettings(provider=str(_require(raw, "rerank.provider"))),
        evaluation=ProviderSettings(provider=str(_require(raw, "evaluation.provider"))),
        observability=ProviderSettings(provider=str(_require(raw, "observability.provider"))),
    )

    validate_settings(settings)
    return settings
