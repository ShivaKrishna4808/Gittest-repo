import pandas as pd

data = {
    "Emp_ID":[1,2,3,4,5],
    "Name":["Raj","Ravi","Ram","Rakesh","Rao"],
    "Salary":[34000,45000,89000,67000,56000]

}

df = pd.DataFrame(data)
df["New_Salary"] = df["Salary"] * 1.1
print(df)