import pandas as pd
import plotly.express as px
from dash import Dash

app = Dash(__name__)

df = pd.read_csv("supermarket_sales.csv")

# data wrangling for the graphs

value = df[['Gender', 'Total']]
value = value.groupby('Gender', as_index=False).sum()
print(value.head())

quantity = df[['Gender', 'Quantity']]
quantity = quantity.groupby('Gender', as_index=False).sum()

product_line_df = df[['Product line', 'Total']]
product_line_df = product_line_df.groupby('Product line', as_index=False).sum()
product_line_df = product_line_df.sort_values('Total')

# This code will deploy 3 different bar charts in 3 different tabs:

# Graph 1: Sales Value by Gender
fig = px.bar(value, x='Gender', y='Total', title='Sales Net Value By Gender in $')
fig.show()

# Graph 2: Quantity of items Sold by gender
fig = px.bar(quantity, x='Gender', y='Quantity', title='Sales Item Quantity By Gender')
fig.show()

# Graph 3: SAlen Net value by product line
fig = px.bar(product_line_df, x='Product line', y='Total', title='Sales net Value by product Line')
fig.show()



