def concatenate_dictionaries(*dicts):
    """
    This function takes multiple dictionaries as input
    and returns a new dictionary that combines all of them.
    """
    result = {}
    for dictionary in dicts:
        result.update(dictionary)
    return result

# Example usage:
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}

combined_dict = concatenate_dictionaries(dic1, dic2, dic3)
print("The concatenated dictionary is:", combined_dict)


#Output

"""
The concatenated dictionary is: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

"""
