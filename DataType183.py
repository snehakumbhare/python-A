#Python: Unique values in a given list of lists

#Write a  Python program to get the unique values in a given list of lists.
# Define a function called 'unique_values_in_list_of_lists' that extracts unique values from a list of lists.
def unique_values_in_list_of_lists(lst):
    result = set(x for l in lst for x in l)  # Flatten the list of lists and create a set to remove duplicates.
    return list(result)  # Convert the set back to a list.

# Create a list of lists 'nums', where each sublist contains integers.
nums = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

# Print a message indicating the original list of lists.
print("Original list:")
print(nums)

# Call the 'unique_values_in_list_of_lists' function with 'nums' and store the unique values.
print("Unique values of the said list of lists:")
# Print the unique values extracted from the list of lists.
print(unique_values_in_list_of_lists(nums))

# Create a list of lists 'chars', where each sublist contains characters.
chars = [['h', 'g', 'l', 'k'], ['a', 'b', 'd', 'e', 'c'], ['j', 'i', 'y'], ['n', 'b', 'v', 'c'], ['x', 'z']]

# Print a message indicating the original list of lists.
print("\nOriginal list:")
print(chars)

# Call the 'unique_values_in_list_of_lists' function with 'chars' and store the unique values.
print("Unique values of the said list of lists:")
# Print the unique values extracted from the list of lists.
print(unique_values_in_list_of_lists(chars)) 
