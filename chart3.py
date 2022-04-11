import gviz_api

page_template = """
<html>
  <head>
  <title>Static example</title>
    <script src="http://www.gstatic.com/charts/loader.js" 
    type="text/javascript"></script>
    <script>
      google.charts.load('current', {packages:['corechart']});
      google.charts.setOnLoadCallback(drawChart);
      function drawChart() {
      var data = google.visualization.arrayToDataTable([
      ['Sales','Sales per Day'],
      ['Jones',19],
      ['Smith',22],
      ['Davis',12],
      ['Johnson',21],
      ['Lewis',17]
      ]);
      
      var options = {title:'Company Daily Sales March'};
      
      var chart = new google.charts.line(document.getElementById('chart'));
      
      chart.draw(data,options); 
      }
    </script>
  </head>
  <body>
    <div id="chart" style="width:900px;height:500px;"></div>
  </body>
</html>
"""

# Putting the JS code and JSon string into the template
print(page_template)
