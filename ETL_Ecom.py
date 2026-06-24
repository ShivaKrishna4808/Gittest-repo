import os
import sys
from pathlib import Path

java_17_home = Path("/opt/homebrew/opt/openjdk@17")
if java_17_home.exists():
    os.environ["JAVA_HOME"] = str(java_17_home)

os.environ["PYSPARK_DRIVER_PYTHON"] = sys.executable
os.environ["PYSPARK_PYTHON"] = sys.executable




from pyspark.sql import SparkSession
from pyspark.sql.functions import *

spark = SparkSession.builder.appName("Ecommerce_ETL").getOrCreate()

orders_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("ecommerce_orders.csv")

orders_df = orders_df.dropDuplicates()

orders_df = orders_df.withColumn("order_date", to_date(col("order_date"), "yyyy-MM-dd") )

orders_df = orders_df.withColumn("revenue", col("quantity") * col("amount"))

orders_df = orders_df.withColumn("year", year(col("order_date"))) \
    .withColumn("month", month(col("order_date")))  

category_sales = orders_df.groupBy("category") \
    .agg(sum("revenue").alias("total_revenue"), count("order_id").alias("total_orders"),avg("revenue").alias("avg_order_value"))

category_sales.show()

category_sales.write \
    .mode("overwrite") \
    .parquet("data/processed/category_sales")

print("ETL Completed")

spark.stop()