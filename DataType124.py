#Python: Find the maximum and minimum product from the pairs of tuple within a given list

#Write a Python program to find the maximum and minimum product of pairs of tuples within a given list.
# Define a function 'tuple_max_val' that finds the maximum and minimum product of pairs in a list of tuples
def tuple_max_val(nums):
    # Calculate the maximum product using list comprehension with abs
    result_max = max([abs(x * y) for x, y in nums])
    # Calculate the minimum product using list comprehension with abs
    result_min = min([abs(x * y) for x, y in nums])
    # Return the maximum and minimum product as a tuple
    return result_max, result_min

# Create a list 'nums' containing tuples of integers
nums = [(2, 7), (2, 6), (1, 8), (4, 9)]
# Print a message indicating the original list of tuples
print("The original list, tuple:")
# Print the contents of 'nums'
print(nums)
# Print a message indicating the operation to find the maximum and minimum product
print("\nMaximum and minimum product from the pairs of the said tuple of list:")
# Call the 'tuple_max_val' function with 'nums' and print the result
print(tuple_max_val(nums))
