"""Thin wrappers around pandas readers for files in ``data/``."""

from __future__ import annotations

from pathlib import Path

import pandas as pd

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = REPO_ROOT / "data"


def data_path(name: str) -> Path:
    """Resolve a filename inside the repo's ``data/`` directory."""
    return DATA_DIR / name


def load_csv(name: str, **kwargs) -> pd.DataFrame:
    """Read a CSV from ``data/`` (or an absolute path) into a DataFrame."""
    path = Path(name)
    if not path.is_absolute():
        path = data_path(name)
    return pd.read_csv(path, **kwargs)


def load_excel(name: str, sheet_name: str | int | None = 0, **kwargs) -> pd.DataFrame:
    """Read an Excel sheet from ``data/`` (or an absolute path)."""
    path = Path(name)
    if not path.is_absolute():
        path = data_path(name)
    return pd.read_excel(path, sheet_name=sheet_name, **kwargs)
