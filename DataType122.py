#Python: Find common element(s) in a given nested lists

#Write a Python program to find common elements in a nested list.
# Define a function 'common_in_nested_lists' that finds common elements in nested lists
def common_in_nested_lists(nested_list):
    # Use set operations to find the common elements in the nested lists
    result = list(set.intersection(*map(set, nested_list)))
    # Return the 'result' list containing the common elements
    return result

# Create a nested list 'nested_list' with sublists containing integer values
nested_list = [[12, 18, 23, 25, 45], [7, 12, 18, 24, 28], [1, 5, 8, 12, 15, 16, 18]]
# Print a message indicating the original lists
print("\nOriginal lists:")
# Print the contents of 'nested_list'
print(nested_list)
# Print a message indicating the operation to find common elements in the nested lists
print("\nCommon element(s) in nested lists:")
# Call the 'common_in_nested_lists' function with 'nested_list' and print the result
print(common_in_nested_lists(nested_list)) 
