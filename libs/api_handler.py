# LIBRARIES
# --------------------------------------------------
import requests
import json

# VARIABLES
# --------------------------------------------------

# user_token for authentication to the api
#auth = ('squ_9087310406db8aa1fef74eeace5f181271adef54', '') # g.ziu's
#url_base = "https://sonarqube.websolute.it/api/"

auth = ('squ_b02ff45095516d7d8652dbbb03903fbd53b369ed', '') # localhost
url_base = "http://localhost:9000/api/"


# FUNCTIONS
# --------------------------------------------------
def get_api_data(section, params = {}, only_section = False):
    try:
        response = requests.get(url_base + section, params, auth = auth)
    except KeyError:
        print("Unvalid section name.")
        exit()
    if response.status_code != 200:
        print("Status code: " + str(response.status_code) + "\n")
        print(response.url + "\n")
        print(response.text)
        exit()
    if only_section == False:
        return response
    return response.json()[section]


def get_api_json(path, params = {}, let_pass = False):
    try:
        response = requests.get(url_base + path, params, auth = auth)
    except KeyError:
        print("Unvalid path name.")
        return False

    x = response.status_code
    if x < 200:
        return 200
    elif x < 300:
        pass
    elif x > 300 and not let_pass:
        print("Something went wrong\n")
        print("Status code: " + str(response.status_code) + "\n")
        print(response.text)
        exit()
    elif x < 400:
        return 400
    elif x < 500:
        return 500
    elif x < 600:
        return 600
    # print("Status code: " + str(response.status_code) + "\n")
    # print(response.url + "\n")
    return response.json()

def get_api_json_mltpl_pages(path, node, params = {}):
    output = []
    p = 1
    while True:
        params.update({"p": p})
        response = get_api_json(path, params, True)
        if type(response) != dict or len(response[node]) == 0:
            break
        output += response[node]
        p += 1
    return output
