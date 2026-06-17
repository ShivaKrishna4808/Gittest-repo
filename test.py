import pandas as pd

data={
    "Name":["Ram",'John','David'],
    "Age": [25,30,35],
    "City":["Hyderabad",'Chennai','Bangalore']
}

df = pd.DataFrame(data)
print(df)
