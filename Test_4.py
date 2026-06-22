import pandas as pd

df = pd.read_csv("Book(Sheet1).csv")
highest_Salary= df[df["SALARY"] == df["SALARY"].max()]
print(highest_Salary)