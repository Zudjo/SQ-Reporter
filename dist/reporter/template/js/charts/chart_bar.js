  function draw_bar_chart(id, title, array_values) {
    // Set Data
    array_values.unshift(["Typology", "Quantity", { role: 'style' }, { role: 'annotation' }])

    var data = google.visualization.arrayToDataTable(
      array_values
      );

    // Set Options
    var options = {
      title: title,
      legend: "none",
      height: "100%",
      width: "100%",
      hAxis: {
        format:'#',
        viewWindow: {
          min: 0
        },
      },
      chartArea: {
        left: "25%",
        right: "0%"
      }
    };

    // Draw Chart
    var chart = new google.visualization.BarChart(document.getElementById(id));
    chart.draw(data, options);
  }
