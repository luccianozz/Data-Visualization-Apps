import gviz_api

page_template = """
<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['line']});
      google.charts.setOnLoadCallback(drawChart);
      google.charts.load('current', {'packages':['line','corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
      var chartDiv = document.getElementById('chartDiv');
      var data = new google.visualization.DataTable();
      data.addColumn('date','Month');
      data.addColumn('number','Total Sales Value');
      data.addRows([
      [new Date(2019,1),116291.868],
      [new Date(2019,2),97219.374],
      [new Date(2019,3),109455.507],
      ]);

      var materialOptions = {
      chart: {
      title:'Total Sales Value fo the First Quarter'},
      width: 900,
      height: 500,
      series: {
      0: {axis: 'Total Sales Value'},
      },
      axes: {
      y: {
      Temps: {label: 'Total Sales Value'},
      }
      }};

      function drawMaterialChart()
      {
      var materialChart = new google.charts.Line(chartDiv);
      materialChart.draw(data,materialOptions);

      }      
      drawMaterialChart();
      }
    </script>
  </head>
  <body>
    <div id="chartDiv"></div>
  </body>
</html>
"""

# Putting the JS code and JSon string into the template
print(page_template)