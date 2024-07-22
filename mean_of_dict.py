def calculate_mean(dictionary):
    """
    This function takes a dictionary of values as input
    and returns the mean of the values.
    """
    # Get the list of values from the dictionary
    values = dictionary.values()
    
    # Calculate the sum of the values
    total_sum = 0
    for value in values:
        total_sum += value
    
    # Calculate the mean by dividing the total sum by the number of values
    mean = total_sum / len(values)
    
    return mean

# Example usage:
test_dict = {"A" : 6, "B" : 9, "C" : 5, "D" : 7, "E" : 4}
mean_value = calculate_mean(test_dict)
print("The mean of the dictionary values is:", mean_value)

#Output
"""
The mean of the dictionary values is: 6.2
"""
