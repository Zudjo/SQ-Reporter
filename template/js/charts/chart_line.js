  function draw_line_chart(id, title, x_title, y_title, array_values) {
    if (array_values[0] == []) {
      console.log("Array of values is empty. Function call abolished.");
      return -1;
    }

    // Set Data
    array_values.unshift([x_title, y_title, { role: 'annotation' }]);

    var data = google.visualization.arrayToDataTable(array_values);

    // Set Options
    var options = {
      title: title,
      legend: "none",
      height: "100%",
      width: "100%",
      hAxis: {
        title: x_title,
        format:'#',
      },
      vAxis: {title: y_title},
      chartArea: {
        left: "15%",
        right: "5%"
      },
      viewWindow: {
        min: 1
      }

    };

    // Draw Chart
    var chart = new google.visualization.LineChart(document.getElementById(id));
    chart.draw(data, options);
  }
