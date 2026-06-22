import pandas as pd

data = {
    "Name": ["Ram", "Sita", "Lakshman"],
    "Department":["IT","HR","IT"],
    "Salary":[50000,45000,48000]
}
df = pd.DataFrame(data)
result = df.groupby("Department")["Salary"].mean()
print(result)

