import sys
import polars as pl

DATA_PATH = '2024_fb_ads_president_scored_anon.csv'
if len(sys.argv) > 1:
    DATA_PATH = sys.argv[1]

df = pl.read_csv(DATA_PATH)

print("=== Basic Descriptive Statistics ===")
print(df.describe())

print("\n=== Number of Unique Values (Top 10 Columns) ===")
for col in df.columns[:10]:
    print(f"{col}: {df.select(pl.col(col).n_unique()).item()}")

print("\n=== Most Frequent Values (Top 10 Categorical Columns) ===")
for col in df.columns[:10]:
    if df[col].dtype == pl.Utf8:
        vc = df.select(pl.col(col).value_counts())
        if vc.shape[0] == 0:
            continue
        other_cols = [c for c in vc.columns if c != col]
        if not other_cols:
            continue
        count_col = other_cols[0]
        top = vc.sort(by=count_col, descending=True).limit(1)
        print(f"{col}: {top.to_dicts()[0]}")
