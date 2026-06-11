default:
    @just --list

setup:
    uv sync

test:
    uv run pytest

lint:
    uv run ruff check .

format:
    uv run ruff format .

clean:
    rm -rf .venv __pycache__ .pytest_cache .ruff_cache

# Launch the marimo notebook server (edit mode)
marimo notebook="notebooks/example.py":
    uv run marimo edit {{notebook}}

# Launch JupyterLab
jupyter:
    uv run jupyter lab --notebook-dir=notebooks
