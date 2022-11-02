# LIBRARIES
# __________________________________________________
from libs.api_handler import *
from libs.json_handler import *
from libs.files_handler import *
from libs.html_handler import *
from libs.calculator import *

# VARIABLES
# __________________________________________________
from data.paths import *
from data.parameters import *
from data.ratings import *

from data.info_dicts.issues import *
from data.info_dicts.hotspots import *

# MAIN
# __________________________________________________

# -------------------------
# Getting data
# -------------------------

# Getting issues data
issues_data = get_api_json("issues/search", issues_parameters)
issues_total = get_node(issues_data, "total")
issues = get_node(issues_data, "issues")
issues = get_api_json_mltpl_pages("issues/search", "issues", issues_parameters)

# Getting analyses dates
analyses_data = get_api_json("project_analyses/search", analyses_parameters)
analyses = get_node(analyses_data, "analyses")
analyses_dates = get_values_by_property_name(analyses, "date", True)

# Getting ratings data
ratings_data = get_api_json("measures/component", ratings_parameters)
ratings = get_node(ratings_data, "component/measures")

# Getting hotspots data
hotspots_data = get_api_json("hotspots/search", hotspots_parameters)
hotspots = get_node(hotspots_data, "hotspots")


# -------------------------
# Elaborating data
# -------------------------

# Counting issues for each analyses date
issues_descending = count_presences_in_property(issues, "closeDate", analyses_dates)

if len(issues_descending) == 0:
    print("This project has no line chart, because no issues were closed.")
else:
    issues_descending = get_descending(issues_descending, issues_total)
    # issues_descending = equalize_with_lowest_to_zero(issues_descending)

# Counting quantities of all groups of issues
issues_properties_quantity = count_properties_per_mltpl_groups(issues, issues_info)

hotspots_properties_quantity = count_properties_per_mltpl_groups(hotspots, hotspots_info)

# -------------------------
# Formatting data for html
# -------------------------

# Formatting for issues line chart
if len(issues_descending):
    issues_descending = get_formatted_line_chart_data(issues_descending, 1)
# Formatting for ratings table
ratings = compose_ratings(ratings_data["component"]["measures"], ratings_letters, ratings_metrics, ratings_intervals)

# Composing bar charts
bar_issues_charts = compose_mltpl_bar_charts(issues_properties_quantity, issues_info)
line_issues_chart = compose_line_chart("issues", "Analyses", "Quantity", issues_descending)

# Formatting hotspots
hotspots = compose_hotspots(hotspots_properties_quantity)

# -------------------------
# Filling template with data
# -------------------------
index = get_file_as_string(path_index)

index = index.format(
    project_key=project_key,
    line_issues_chart=line_issues_chart,
    bar_issues_charts=bar_issues_charts,
    ratings=ratings,
    hotspots=hotspots
)

# -------------------------
# Outputting data
# -------------------------
write_file(path_temp_index, index, True)
convert_to_pdf(path_temp_index, path_output)
delete_file(path_temp_index)

input("\nExecution completed, press anything to close...")
