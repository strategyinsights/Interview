import marimo

__generated_with = "0.9.0"
app = marimo.App(width="medium")


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell
def _(mo):
    mo.md(
        """
        # Example analytics notebook

        Drop a CSV into `data/` and read it with the shared helper. Edit this
        notebook freely or copy it as a starting point for new analyses.
        """
    )
    return


@app.cell
def _():
    import pandas as pd

    from analytics.io import DATA_DIR, load_csv

    sample_path = DATA_DIR / "example.csv"
    if not sample_path.exists():
        pd.DataFrame(
            {
                "month": ["2026-01", "2026-02", "2026-03"],
                "revenue": [100, 130, 165],
            }
        ).to_csv(sample_path, index=False)

    df = load_csv("example.csv")
    return DATA_DIR, df, load_csv, pd, sample_path


@app.cell
def _(df):
    df
    return


@app.cell
def _(df):
    ax = df.plot(x="month", y="revenue", marker="o", title="Revenue by month")
    ax.figure
    return (ax,)


if __name__ == "__main__":
    app.run()
