import pandas as pd

df = pd.read_parquet("train.parquet")
result = df.describe(include="all")

result.to_json("dataset_describe.json")
