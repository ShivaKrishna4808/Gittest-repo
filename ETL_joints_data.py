from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("BankingLeftJoin").getOrCreate()

customer_data = [
    (101,"Ravi","Guntur"),
    (102,"Sita","Vijayawada"),
    (103,"Kumar","Hyderabad"),
    (104,"Anil","Chennai")
]

account_data = [
    ("A001",101,"Savings",50000),
    ("A002",102,"Current",650000),
    ("A003",103,"Savings",250000)

]

customer_df = spark.createDataFrame(customer_data,["customer_id","customer_name","city"])

account_df = spark.createDataFrame(account_data,["account_id","customer_id","account_type","balance"])

result_df = customer_df.alias("c").join(account_df.alias("a"),customer_df.customer_id == account_df.customer_id,"left").select("c.customer_id","c.customer_name","c.city","a.account_id","a.account_type","a.balance")

result_df.show(truncate=False)

spark.stop()
