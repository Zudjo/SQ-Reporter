# LIBRARIES
# __________________________________________________


# VARIABLES
# __________________________________________________
#from data.info_dicts.issues import *
#from data.info_dicts.issues import *

# FUNCTIONS
# __________________________________________________

def get_node(json, node_name):
    try:
        return [json := json[nd] for nd in node_name.split("/")][-1]
    except TypeError:
        print("The section path is ambigous or doesn't exists.\n\nSection path: " + str(node_name))
        exit()


def get_values_by_property_name(node, property_name, sorted = False):
    values = []

    for property in node:
        values.append(property[property_name])

    if sorted:
        values.sort()
        return values
    return values


def count_presences_in_property(json, property_name, property_values = []):
    # counts how many times the couple "property_name:property_value" is present,
    # for each value of the property_values list
    # returns a list with the counted number of each value

    property_values_len = len(property_values)
    counted = [0] * (property_values_len + 1)

    for node in json:
        for property in range(property_values_len):
            try:
                if node[property_name] == property_values[property]:
                    counted[property] += 1
                    break
            except KeyError:
                if node["status"] == "RESOLVED":
                    counted[property_values_len - 1] += 1
                    break
                counted[property_values_len] += 1
                break

    return counted


def count_properties_per_group(json, group_name, info_dict):
    properties = info_dict[group_name].keys()

    # Initialization of values
    values = {}
    for property in properties:
        values.update({property: 0})

    # Counting
    for node in json:
        try:
            if (group_name == "type" or group_name == "severity") and (node["status"] == "CLOSED" or node["status"] == "RESOLVED"):
                pass
            else:
                values[node[group_name]] += 1
        except KeyError:
            pass
    return values


def count_properties_per_mltpl_groups(json, info_dict):
    groups_names = info_dict.keys()
    values = []

    for group_name in groups_names:
        properties_quantities = count_properties_per_group(json, group_name, info_dict)

        values_group = {}
        for property in info_dict[group_name]:
            values_group.update({property: 0})

        for property in properties_quantities:
            updated = {property: values_group[property] + properties_quantities[property]}
            values_group.update(updated)
        values.append(values_group)
    return values
