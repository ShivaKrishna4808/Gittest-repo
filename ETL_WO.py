from pyspark.sql import SparkSession
from pyspark.sql.functions import (col,when,avg,sum,count,dense_rank,current_date,datediff,round)
from pyspark.sql.window import Window
spark = SparkSession.builder.appName("AdvancedEmployeeAnalytics").getOrCreate()

employee_data = [
    (101,"John","IT",85000,"2020-01-15"),
    (102,"Alice","HR",65000,"2019-03-20"),
    (103,"Kia","IT",90000,"2018-03-10"),
    (104,"David","Finance",78000,"2021-05-12"),
    (105,"Eva","IT",69000,"2022-02-18")

]

employee_df = spark.createDataFrame(employee_data,["Emp_id","Emp_Name","Department","Salary","Joined_Date"])

dept_data = [
    ("IT",500000),
    ("HR",200000),
    ("Finance",300000)

]

dept_df = spark.createDataFrame(dept_data,["Department","Budget"])


employee_df =employee_df.withColumn(
    "Experience_days",
    datediff(current_date(),
col("Joined_date")))



employee_df = employee_df.withColumn(
    "Salary_grade",
    when(col("Salary")>=90000,"A")
    .when(col("Salary")>= 75000,"B")
    .otherwise("C")

)

Joined_df = employee_df.join(dept_df,on = "Department",how="left")

dept_status = Joined_df.groupBy("Department").agg(count("*").alias("Employee_count"),round(avg("Salary"),2).alias("avg_salary"),sum("Salary").alias("Total_salary"))

dept_status.show()

salary_window =  Window.partitionBy("Department").orderBy(col("Salary").desc())

ranked_df = Joined_df.withColumn("Salary_rank",dense_rank().over(salary_window))

ranked_df.show()

top_employee_df=ranked_df.filter(col("Salary_rank")==1)

top_employee_df.show()

running_window = Window.partitionBy("Department").orderBy("Salary")

running_df = ranked_df.withColumn("running_salary_total",sum("Salary").over(running_window.rowsBetween(Window.unboundedPreceding,Window.currentRow)))

running_df.show()

dept_total_window = Window.partitionBy("Department")

contribution_df = running_df.withColumn("Dept_Total_Salary",sum("Salary").over(dept_total_window)).withColumn("Salary_Contribution_pct",round((col("Salary")/col("dept_total_salary"))*100,2))

contribution_df.show()

contribution_df.cache()

contribution_df.select(
    "Emp_id","Emp_name","Department","Salary","Salary_rank","Salary_grade","Salary_contribution_pct"
).show()


spark.stop()



