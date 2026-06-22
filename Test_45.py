import pandas as pd 

df = pd.read_csv("employee_sheet.csv")

df = df.sort_values(by = "Salary",ascending=True)

print(df)