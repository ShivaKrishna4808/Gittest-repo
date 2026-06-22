# # from pyspark.sql import SparkSession

# # spark = SparkSession.builder \
# #     .appName("smitum") \
# #     .getOrCreate()

# # data = [
# #     (1),(2),(3),(4),(5),(6),(7),(8),(9),(10)
# # ]

# # df = spark.createDataFrame(data,["number"])

# # df.filter("Number % 2 = 0").show()



# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("smitum") \
#     .getOrCreate()

# data = [
#     (1),(2),(3),(4),(5),(6),(7),(8),(9),(10)
# ]

# df = spark.createDataFrame(data,["number"])

# df.filter("Number % 2 = 0").show()

from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("smitum") \
    .getOrCreate()

data = [
    (1,), (2,), (3,), (4,), (5,),
    (6,), (7,), (8,), (9,), (10,)
]

df = spark.createDataFrame(data,["number"])

df.filter("Number % 3 == 0").show()

spark.stop()