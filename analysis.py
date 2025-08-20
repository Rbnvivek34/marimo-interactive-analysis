import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import marimo

@marimo.app
def app():
    import marimo as mo

    # Load CSV (provided in repo)
    df = pd.read_csv("correlation.csv")

    # Slider widget
    x = mo.ui.slider(1, 100, 10)

    # Markdown output
    mo.md(f"Slider value: **{x.value}**")

    # Correlation heatmap
    fig, ax = plt.subplots(figsize=(8, 6))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    mo.mpl(fig)

    return []
  
