# Data Visualization Techniques
___
## Google Visualization Graphs:
### Chart 1: Sales.html

The graph is designed to show how the total sales value was driven 
along the first quarter of the year, this is strategic analysis and
the chart would grow as long the rest of the year advances. I did just 
one quarter since the dataset just held data for the first 3 months of the year.

### Chart 2: Product.html

The chart is designed to display in an Excel sheet type of chart the values of the product categories
in terms of sales value. This could go integrated with the line chart and might be filtered to see
how each product categories developed along the first quarter.

___
## Dash Visualization Graphs
**Using dash and plotly libraries**
```
    pip install plotly
    pip install dash
```

### Chart 3: chart3.py

In this chart we are plotting three different graphs, one is based on the distribution of net sales value
by gender plotted on a bar chart. The second one is a distribution among quantity in order to understand if 
there's any variation of price vs quantity among gender, There's not. Finally, the last graph is a histogram 
based distribution of  the product line categories by net price value in order to understand if there's much 
variation from product to product, concluding that there's not.

To run the code:
```
python chart3.py
```
### Chart 4: chart4.py
On this graph I used a different dataset, I chose to use a supply chain data set in order to understand
some product line value distribution among time. For this I made a line chart that showed me how it
exponentially increased over time.

To run the code:
```
python chart4.py
```