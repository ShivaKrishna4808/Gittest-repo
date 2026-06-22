from pyspark.sql import SparkSession
from pyspark.sql.functions import when 
from pyspark.sql.functions import avg
from pyspark.sql.functions import desc
from pyspark.sql.functions import count
from pyspark.sql.window import Window
from pyspark.sql.functions import rank
from pyspark.sql.functions import row_number

spark = SparkSession.builder.appName("StudentExample").getOrCreate()

students = [
    (1,"Rahul",20,"CSE",85),
    (2,"Priya",21,"ECE",91),
    (3,"Srinu",32,"CSE",86),
    (4,"Venkat",21,"ECE",76),
    (5,"Ravi",22,"EEE",65)
]

columns = ["student_id","Name","Age","Department","Marks"]

df = spark.createDataFrame(students,columns)

df.show()

df.select ("Name","Marks").show()
# df.select ("Name","Marks > 90").show()
df.filter(df.Marks >90).show()

df = df.withColumn(
    "Grade",
    when(df.Marks >= 90, "A")
    .when(df.Marks >= 80, "B")
    .otherwise("C")
)

df.show()

df.groupBy("Department").agg(avg("Marks").alias("avg_Marks")).show()

df.orderBy(desc("Marks")).show(2)

df.groupBy("Department").agg(count("*").alias("Student_count")).show()

window_spec = Window.orderBy(df.Marks.desc())

ranked_df = df.withColumn(
    "Rank",rank().over(window_spec)
)
ranked_df.show()

df.createOrReplaceTempView("StudentsExample")

spark.sql("""SELECT Department,AVG(Marks) AS avg_Marks
          from StudentsExample
          group by Department""").show()


result = df.withColumn(
    "Status",
    when(df.Marks >= 40,"Pass").otherwise("Fail")
)
result.show()


window_spec = Window.partitionBy("Department").orderBy(df.Marks.desc())

top_students = df.withColumn("Row_num",row_number().over(window_spec)).filter("Row_num <= 2")

top_students.show()

