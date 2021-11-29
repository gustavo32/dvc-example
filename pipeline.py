from google.cloud import bigquery


bqclient = bigquery.Client()

query_string = """
SELECT product_id, price, category, volume
FROM `sandbox-ml-pipeline.featurestore.history`
WHERE product_id in ('4', '5', '6')
"""

dataframe = (
    bqclient.query(query_string)
    .result()
    .to_dataframe(
        create_bqstorage_client=True
    )
)

train = dataframe[:8]
test = dataframe[8:]

print(train.dtypes)

train.to_parquet("train.parquet")
test.to_parquet("test.parquet")
print(dataframe)
