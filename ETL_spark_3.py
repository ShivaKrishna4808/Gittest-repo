from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Department") \
    .getOrCreate()

data = [
    ("IT"),
    ("HR"),
    ("IT"),
    ("HR"),
    ("IT"),
    ("Finance")
]

df = spark.createDataFrame([(x,) for x in data], ["Department"])

df.groupBy("Department").count().show()

