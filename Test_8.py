import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Lakshman","Ravi","Krishna"],
    "Department":["IT","HR","Finace","IT","HR"],
    "Salary":[50000,45000,44000,23780,32900]
}
df = pd.DataFrame(data)

result = df.groupby("Department")["Salary"].mean()
print(result)