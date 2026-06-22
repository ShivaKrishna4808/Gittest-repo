import pandas as pd

sales = {
    "Product":["Laptop","Mobile","Laptop","Tablet"],
    "Amount":[55000,34678,67000,12000]
}

df = pd.DataFrame(sales)

total_sales = df["Amount"].sum()
print("Total_Sales:", total_sales)

product_sales = df.groupby("Product")["Amount"].sum()
print("Product_sales:",product_sales)