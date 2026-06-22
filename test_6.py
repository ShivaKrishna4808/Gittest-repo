import pandas as pd

df = pd.read_csv("employee_sheet.csv")

df["Hike"] = df["Salary"] * 0.11

print(df)   