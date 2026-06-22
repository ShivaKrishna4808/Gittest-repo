import pandas as pd

df = pd.read_csv("employee_sheet.csv")

result = df[df["Salary"] > 55000]

print(result)