import pandas as pd

df = pd.read_csv("data/raw/02_nav_history.csv")

print(df.columns.tolist())
print("\nShape:", df.shape)
print("\nFirst 5 rows:")
print(df.head())