#Python: Sum two or more lists, the lengths of the lists may be different

#Write a  Python program to sum two or more lists. The lengths of the lists may be different.

# Define a function called 'sum_lists_diff_length' that calculates the sum of lists with different lengths.
def sum_lists_diff_length(test_list):
    # Create a result list using a list comprehension.
    # 1. For each sublist 'x' in 'test_list', calculate the sum of its elements.
    # 2. Use 'zip(*map(...))' to ensure that all sublists have the same length by padding shorter sublists with zeros.
    result = [sum(x) for x in zip(*map(lambda x: x + [0] * max(map(len, test_list)) if len(x) < max(map(len, test_list)) else x, test_list))]
    return result  # Return the list of sums.

# Create a list of lists 'nums', where each sublist contains integers.
nums = [[1, 2, 4], [2, 4, 4], [1, 2]]

# Print a message indicating the original list of lists.
print("\nOriginal list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the sum of lists with different lengths.
print("Sum said lists with different lengths:")
# Call the 'sum_lists_diff_length' function with 'nums' and print the result (sums of sublists).
print(sum_lists_diff_length(nums))

# Create another list of lists 'nums' with different lengths.
nums = [[1], [2, 4, 4], [1, 2], [4]]

# Print a message indicating the original list of lists.
print("\nOriginal list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the sum of lists with different lengths.
print("Sum said lists with different lengths:")
# Call the 'sum_lists_diff_length' function with 'nums' and print the result (sums of sublists).
print(sum_lists_diff_length(nums)) 
