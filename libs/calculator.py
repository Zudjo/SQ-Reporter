# LIBRARIES
# __________________________________________________


# VARIABLES
# __________________________________________________
#from data.issues import *

excluded_issues = 0

# FUNCTIONS
# __________________________________________________

# Calculating issues descend (left overed issues after each analyses)
def get_descending(values, total):
    for value in range(len(values)):
        if not value:
            values[value] = total - values[value]
        else:
            values[value] = values[value - 1] - values[value]
    #values.pop()
    return values


def equalize_with_lowest_to_zero(array):
    array_length = len(array)
    y = array[array_length - 1]
    for x in range(array_length):
        array[x] -= y
    return array


#def remove_excluded_issues(descending):
