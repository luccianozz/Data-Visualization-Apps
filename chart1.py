import gviz_api

page_template = """
<html>
  <head>
  <title>Static example</title>
    <script src="http://www.google.com/jsapi" type="text/javascript"></script>
    <script>
      google.load("visualization", "1", {packages:["table"]});
      google.setOnLoadCallback(drawTable);
      function drawTable() {
        %(jscode)s
        var jscode_table = new google.visualization.Table(document.getElementById('table_div_jscode'));
        jscode_table.draw(jscode_data, {showRowNumber: true});
        var json_table = new google.visualization.Table(document.getElementById('table_div_json'));
        json_table.draw(json_data, {showRowNumber: true});
      }
    </script>
  </head>
  <body>
    <H1>Table for Product Categories by Total Sales Value</H1>
    <div id="table_div_jscode"></div>
  </body>
</html>
"""


def main():
    # Creating the data
    description = {"Product Line": ("string", "Product Line"),
                   "Total Sales": ("number", "Salary")}
    data = [{"Product Line": "Health and beauty", "Total Sales": (49193.7390, "$49193.7390")},
            {"Product Line": "Home and lifestyle", "Total Sales": (53861.9130, "$53861.9130")},
            {"Product Line": "Fashion accessories", "Total Sales": (54305.8950, "$54305.8950")},
            {"Product Line": "Electronic accessories", "Total Sales": (54337.5315, "$54337.5315")},
            {"Product Line": "Sports and travel", "Total Sales": (55122.8265, "$55122.8265")}]

    data_table = gviz_api.DataTable(description)
    data_table.LoadData(data)

    jscode = data_table.ToJSCode("jscode_data",
                                 columns_order=("Product Line", "Total Sales"),
                                 order_by="Total Sales")
    print(page_template % vars())


if __name__ == "__main__":
    main()
