import pandas as pd

df = pd.read_csv("dataset/HAM10000_metadata.csv")

print(df.head())
print(df.columns)
print(df["dx"].value_counts())