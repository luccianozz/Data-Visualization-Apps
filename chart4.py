import pandas as pd
import plotly.express as px
from dash import Dash

app = Dash(__name__)

# Supply chain dataset: https://www.kaggle.com/datasets/divyeshardeshana/supply-chain-shipment-pricing-data?resource=download
df = pd.read_csv("SCMS_Delivery_History_Dataset.csv")

# Data wrangling
deliver_date_df = df[['Delivery Recorded Date', 'Line Item Value']]
deliver_date_df['Delivery Recorded Date'] = pd.to_datetime(deliver_date_df['Delivery Recorded Date'])
deliver_date_df['year'] = deliver_date_df['Delivery Recorded Date'].dt.to_period('Y')
deliver_date_df['year'] = deliver_date_df['year'].astype(str)
deliver_date_df = deliver_date_df.groupby('year', as_index=False).sum()

# Plotting
fig = px.line(deliver_date_df,
              x="year",
              y="Line Item Value",
              title='Line Item Value (USD) by Date in Supply Chain Data Set')
fig.show()

