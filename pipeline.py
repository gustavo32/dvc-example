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

train = dataframe[:8]
test = dataframe[8:]

train.to_csv("train.csv")
test.to_csv("test.csv")
print(dataframe)
