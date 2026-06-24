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


spark = SparkSession.builder \
    .appName("Sales_ETL") \
    .master("local[*]") \
    .getOrCreate()

sales_df = spark.read \
    .option("header", True) \
    .option("inferSchema", True) \
    .csv("sales.csv")

sales_df = sales_df.dropDuplicates()

sales_df = sales_df.fillna({"quantity": 1})

sales_df = sales_df.filter(col("price").isNotNull())

sales_df = sales_df.withColumn(
    "order_date",
    to_date(col("order_date"), "yyyy-MM-dd")
)

sales_df = sales_df.withColumn(
    "revenue",
    col("quantity") * col("price")
)

sales_df = sales_df \
    .withColumn("year", year(col("order_date"))) \
    .withColumn("month", month(col("order_date")))

daily_sales = sales_df.groupBy("order_date") \
    .agg(
        sum("revenue").alias("total_revenue"),
        count("order_id").alias("total_orders")
    ) \
    .orderBy("order_date")

daily_sales.show()

daily_sales.write \
    .mode("overwrite") \
    .parquet("data/processed/daily_sales")

print("ETL Completed")

spark.stop()
