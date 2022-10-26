import json

def compose_counted_issues_groups(issues_values, string):
    string.format(*issues_values)
    return string

def get_formatted_line_chart_data(y_values, x_values = 0):
    y_values.pop()
    string = ""

    if type(x_values) == int:
        for y in y_values:
            string += "[{}, {}, {}], ".format(x_values, y, y)
            x_values += 1
    else:
        for n in len(x_values):
            string += "[{}, {}, {}], ".format(x_values[n], y_values[n], y_values[n])

    string = string[:-2]
    return string

def compose_ratings(ratings_list_dict, ratings_letters, ratings_metrics, ratings_intervals):
    string = ""
    for x in ratings_list_dict:
        string += """

            <tr>
                <td class="rating-name">{metric_name}</td>
                <td><span class="rating rating-{r_l}">{r_l}</span></td>
                <td class="rating-criterion">{unit_of_measure}:</td>
                <td class="rating-criterion">{interval}</td>
            </tr>

        """.format(
                r_l = ratings_letters[x["value"]],
                metric_name = ratings_metrics[x["metric"]],
                unit_of_measure = ratings_intervals[x["metric"]]["value"],
                interval = ratings_intervals[x["metric"]][ratings_letters[x["value"]]]
            )

    return string

def compose_hotspots(json):
    return """
        <tr>
            <th>Fixed</th>
            <td>{}</td>
        </tr>
        <tr>
            <th>Safe</th>
            <td>{}</td>
        </tr>
        <tr>
            <th>Acknowledged</th>
            <td>{}</td>
        </tr>
        <tr>
            <th>To review</th>
            <td>{}</td>
        </tr>
        """.format(
                json[1]["FIXED"],
                json[1]["SAFE"],
                json[1]["ACKNOWLEDGED"],
                json[0]["TO_REVIEW"]
            )

def get_formatted_bar_chart_data(id, title, array_values):
    string = """
        id = {id};
        title = {title};
        array_values = {array_values};

        draw_bar_issues_groups_chart(id, title, array_values);
    """.format(
        id = id,
        title = title,
        array_values = array_values
    )
    return string

def compose_line_chart(title, title_x, title_y, chart_values):
    return """
        draw_line_chart("{title}_chart", "{title}", "{title_x}", "{title_y}", [{chart_values}]);
    """.format(
            title = title,
            title_x = title_x,
            title_y = title_y,
            chart_values = chart_values
        )



def compose_bar_chart(values, title, info_dict, tot_excluded):
    chart_values = ""

    for property in info_dict:
        value = values[property]
        color = info_dict[property]["color"]
        chart_values += "['{}', {}, '{}', {}],".format(property, value, color, value)

    chart_values = chart_values[:-1]
    return """
        draw_bar_chart("{title}_chart", "{title}", [{chart_values}]);
    """.format(title = title, chart_values = chart_values)


def compose_mltpl_bar_charts(values, info_dict, tot_excluded = 0):
    charts_calls = ""
    i = 0

    for group in info_dict:
        if group == "type" or group == "severity" or group == "status":
            pass

        charts_calls += compose_bar_chart(values[i], group, info_dict[group], tot_excluded)
        i += 1

    return charts_calls
