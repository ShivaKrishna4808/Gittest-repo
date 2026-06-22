from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("Age-File") \
    .getOrCreate()

data = [
    (1, "John", 25),
    (2, "Mike", 30),
    (3, "David", 35),
    (4, "Sara", 28)
]

df = spark.createDataFrame(data, ["id", "name", "age"])

df.filter(df.age>30).show()