# analytics-starter

Minimum viable Python repo for ad-hoc CSV/Excel analytics. No database
connections — input data lives in `data/` as CSV or Excel files.

## Prerequisites

- Python 3.12
- [uv](https://docs.astral.sh/uv/) (`pipx install uv` or `brew install uv`)
- [just](https://github.com/casey/just) (optional but recommended)

## Quick start

```bash
just setup           # creates .venv and installs deps (incl. notebook + dev)
just marimo          # opens notebooks/example.py in marimo
just jupyter         # alternative: open JupyterLab in notebooks/
just test            # run pytest
just lint            # ruff check
just format          # ruff format
```

Without `just`:

```bash
uv sync
uv run marimo edit notebooks/example.py
uv run jupyter lab --notebook-dir=notebooks
uv run pytest
```

## Layout

```
analytics-starter/
├── data/             # input CSVs / Excel files (committed to git)
├── notebooks/        # marimo (.py) and jupyter (.ipynb) notebooks
├── src/analytics/    # shared helpers importable from notebooks
└── tests/            # pytest tests for src/analytics/
```

## Adding shared code

Anything you want to reuse across notebooks goes in `src/analytics/`. The
`example.py` marimo notebook shows how to import from it.

```python
from analytics.io import load_csv

df = load_csv("data/example.csv")
```

## Adding dependencies

```bash
uv add scikit-learn          # runtime dep
uv add --group dev mypy      # dev-only dep
uv add --group notebook nbconvert
```
