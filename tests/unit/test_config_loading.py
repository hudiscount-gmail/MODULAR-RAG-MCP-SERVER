"""Tests for config loading and validation."""

from __future__ import annotations

from pathlib import Path

import pytest

from core.settings import SettingsError, load_settings


def test_load_settings_happy_path(tmp_path: Path) -> None:
    yaml_path = tmp_path / "settings.yaml"
    yaml_path.write_text(
        """
app:
  name: test-app

llm:
  provider: none
embedding:
  provider: none
vector_store:
  provider: none
retrieval:
  provider: hybrid
rerank:
  provider: none
evaluation:
  provider: none
observability:
  provider: stderr
""".lstrip(),
        encoding="utf-8",
    )

    settings = load_settings(str(yaml_path))
    assert settings.app.name == "test-app"
    assert settings.retrieval.provider == "hybrid"


def test_load_settings_missing_required_field_reports_path(tmp_path: Path) -> None:
    yaml_path = tmp_path / "settings.yaml"
    yaml_path.write_text(
        """
app:
  name: test-app

llm:
  provider: none
embedding:
  provider: none
vector_store:
  provider: none
retrieval:
  provider: hybrid
rerank:
  provider: none
evaluation:
  provider: none
observability: {}
""".lstrip(),
        encoding="utf-8",
    )

    with pytest.raises(SettingsError) as exc:
        load_settings(str(yaml_path))

    assert "observability.provider" in str(exc.value)
