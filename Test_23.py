import pandas as pd

df = pd.read_csv("Book(Sheet1).csv")

df = df.drop_duplicates()
print(df)   

