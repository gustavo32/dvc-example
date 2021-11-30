import pandas as pd
import sys

df = pd.read_parquet("train.parquet")
result = df.describe(include="all")

result.to_json(sys.argv[1])
