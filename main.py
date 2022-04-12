import pandas as pd

# ***************************************************
# * This script is used for chart1.py and chart2.py *
# ***************************************************

# data frame construction
sales_df = pd.read_csv("supermarket_sales.csv")

# Data wrangling
total_sales_df = sales_df[['Date', 'Total']]
total_sales_df['Date'] = pd.to_datetime(total_sales_df['Date'])
total_sales_df['Date'] = total_sales_df['Date'].dt.to_period('M')


# first data frame for the sales.html graph
quarters = total_sales_df.groupby('Date', as_index=False).sum()
print(quarters.head())

# second data fame used for the product.html chart
product_line_df = sales_df[['Product line', 'Total']]
product_line_df = product_line_df.groupby('Product line', as_index=False).sum()
product_line_df = product_line_df.sort_values('Total')
print(product_line_df.head())


quantity = sales_df[['Gender', 'Quantity']]
quantity = quantity.groupby('Gender', as_index=False).sum()
print(quantity.head())
