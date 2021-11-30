from google.cloud import bigquery


bqclient = bigquery.Client()

query_string = """
SELECT product_id, price, category, volume
FROM `sandbox-ml-pipeline.featurestore.history`
WHERE product_id in ('3', '4', '5', '6', '7')
"""

dataframe = (
    bqclient.query(query_string)
    .result()
    .to_dataframe(
        create_bqstorage_client=True
    )
)

train = dataframe[:10]
test = dataframe[10:]

print(train)

# train["volume"] = train.volume.astype("str")
# test["volume"] = test.volume.astype("str")

print(train.dtypes)

train.to_parquet("train.parquet")
test.to_parquet("test.parquet")
print(dataframe)
