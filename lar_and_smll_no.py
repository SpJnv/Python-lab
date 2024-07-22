def find_largest_and_smallest(lst):
    """
    This function takes a list of numbers as input
    and returns the largest and smallest numbers in the list.
    """
    # Check if the list is empty
    if not lst:
        return None, None

    # Initialize the largest and smallest with the first element of the list
    largest = smallest = lst[0]

    # Iterate through the list starting from the second element
    for num in lst[1:]:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

    return largest, smallest

# Example usage:
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
largest, smallest = find_largest_and_smallest(my_list)
print("The largest number in the list is:", largest)
print("The smallest number in the list is:", smallest)


#output
"""
The largest number in the list is: 9
The smallest number in the list is: 1
"""
