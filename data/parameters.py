print("1. Define project key")
print("2. Use default project key (recommended)\n")
choice = input("Choice: ")

if choice == "1":
    project_key = input("Insert project key: ")
else:
    project_key = "BOM-TEST" # default

issues_parameters = {"componentKeys": project_key, "s": "SEVERITY", "ps": "500"}
analyses_parameters = {"project": project_key}
ratings_parameters = {"component": project_key, "metricKeys": "sqale_rating, reliability_rating, security_rating, security_review_rating"}
hotspots_parameters = {"projectKey": project_key}
# badge_token = "squ_9b9cebcb6a1aa6ab72b674720dfce1c58967d3b5" # Baldi-TEST
# badge_token = "squ_b4feabbe7777893f49d64fc82a58df5ac8f8bb4d" # baldi2
# badge_token = "squ_01a6c5bb15c06b1b4ba2b24122a8511256ca3686" # BKT-BIKE
badge_token = "eb0a371a9b4898758d16d6e84d3c0049e09c2d91" # BOM-TEST
