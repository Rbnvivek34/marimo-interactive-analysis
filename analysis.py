# Author: 22f2001699@ds.study.iitm.ac.in

import marimo as mo
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_excel("q-excel-correlation-heatmap.xlsx", sheet_name="Supply_Chain_Data")

# --- Cell 1: Slider widget for filtering ---
slider = mo.ui.slider(70, 100, step=1, label="Minimum Delivery Performance")
slider

# --- Cell 2: Filtered Data based on slider ---
# Data dependency: This depends on slider.value
filtered_df = df[df["Delivery_Performance"] >= slider.value]
filtered_df.head()

# --- Cell 3: Correlation Heatmap ---
# Depends on filtered_df
corr = filtered_df.corr()

fig, ax = plt.subplots(figsize=(6,4))
sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
mo.mpl(fig)

# --- Cell 4: Dynamic Markdown Output ---
# Depends on slider and filtered_df
mo.md(f"""
### 📊 Correlation Heatmap Analysis  
- Currently filtering suppliers with Delivery Performance ≥ **{slider.value}%**  
- Number of records remaining: **{len(filtered_df)}**  

🔎 Adjust the slider to explore how filtering changes correlations!
""")
