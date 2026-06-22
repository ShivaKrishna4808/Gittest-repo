from pyspark.sql import SparkSession
from pyspark.sql.functions import desc


spark = SparkSession.builder.appName("Employee_Info").getOrCreate()

data = [
    (1,"Shiva","HR",98000),
    (2,"krishna","IT",68000),
    (3,"Ram","IT",78000),
    (4,"Rahul","Finace",85000),
    (5,"Sri","HR",96000)
]

colmuns = ["Employee_ID","Name","Department","Salary"]

df = spark.createDataFrame(data,colmuns)

df.show()

df.orderBy(desc("salary")).show(1)


