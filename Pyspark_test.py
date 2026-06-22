from pyspark.sql import SparkSession
from pyspark.sql.functions import sum
from pyspark.sql.functions import col 
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number



spark  = SparkSession.builder.appName("EmployeeDemo").getOrCreate()

data = [
    (1,"John","IT",56000),
    (2,"Raj","HR",45000),
    (3,"Ravi","IT",67000),
    (4,"Shiva","Finace",85000),
    (5,"Krishna","IT",44000)
]

columns= ["Emp_ID","Name","Department","Salary"]

df = spark.createDataFrame(data,columns)
df.show()

# from pyspark.sql import SparkSession

# spark = SparkSession.builder \
#     .appName("EmployeeDemo") \
#     .getOrCreate()

# data = [
#     (1, "John", "IT", 50000),
#     (2, "Mike", "HR", 60000),
#     (3, "David", "IT", 70000),
#     (4, "Sara", "Finance", 55000)
# ]

# columns = ["id", "name", "department", "salary"]

# df = spark.createDataFrame(data, columns)

# df.show()

df.filter(df.Salary > 55000).show()

df.groupBy("Department").agg(sum("Salary").alias("Total_Salary")).show()


df = df.withColumn(
    "Bonus",
    col("Salary") * 0.10

)
df .show()


df.createOrReplaceTempView("EmployeeDemo")

result = spark.sql("""SELECT Name,Salary From EmployeeDemo where salary > 55000""")


result.show()

windowSpec = Window.partitionBy("Department").orderBy(df.Salary.desc())

result = df.withColumn(
    "rank",
    row_number().over(windowSpec)).filter("rank = 1")

result.show()