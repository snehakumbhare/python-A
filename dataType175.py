#Python: Find the minimum, maximum value for each tuple position in a given list of tuples
#Write a  Python program to find the minimum and maximum value for each tuple position in a given list of tuples.
# Define a function called 'max_min_list_tuples' that computes the maximum and minimum values for each position in a list of tuples 'nums'.
def max_min_list_tuples(nums):
    # Use 'zip' to transpose the tuples in 'nums' so that we can work with each position separately.
    zip(*nums)
    # Use 'map' and 'max' to find the maximum value for each position in the transposed tuples.
    result1 = map(max, zip(*nums))
    # Use 'map' and 'min' to find the minimum value for each position in the transposed tuples.
    result2 = map(min, zip(*nums))
    # Convert the results into lists and return them.
    return list(result1), list(result2)

# Create a list of tuples 'nums' containing tuples of integer values.
nums = [(2, 3), (2, 4), (0, 6), (7, 1)]

# Print a message indicating the original list of tuples.
print("Original list:")
print(nums)

# Call the 'max_min_list_tuples' function to compute the maximum and minimum values for each tuple position in the list of tuples 'nums'.
result = max_min_list_tuples(nums)

# Print a message indicating the maximum value for each tuple position in the list of tuples.
print("\nMaximum value for each tuple position in the said list of tuples:")
print(result[0])

# Print a message indicating the minimum value for each tuple position in the list of tuples.
print("\nMinimum value for each tuple position in the said list of tuples:")
print(result[1])

