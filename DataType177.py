#Python: Common elements in a given list of lists

#Write a  Python program to find common elements in a given list of lists.

# Define a function called 'common_list_of_lists' that finds the common elements among multiple lists 'lst'.
def common_list_of_lists(lst):
    # Use set intersection to find the common elements among the lists in 'lst'.
    temp = set(lst[0]).intersection(*lst)
    # Convert the result into a list and return it.
    return list(temp)

# Create a list of lists 'nums' containing sublists of integers.
nums = [[7, 2, 3, 4, 7], [9, 2, 3, 2, 5], [8, 2, 3, 4, 4]]

# Print a message indicating the original list of lists.
print("Original list:")
print(nums)

# Call the 'common_list_of_lists' function to find the common elements among the sublists in 'nums' and print the result.
print("\nCommon elements of the said list of lists:")
print(common_list_of_lists(nums))

# Create a list of lists 'chars' containing sublists of characters.
chars = [['a', 'b', 'c'], ['b', 'c', 'd'], ['c', 'd', 'e']]

# Print a message indicating the original list of lists.
print("\nOriginal list:")
print(chars)

# Call the 'common_list_of_lists' function to find the common elements among the sublists in 'chars' and print the result.
print("\nCommon elements of the said list of lists:")
print(common_list_of_lists(chars)) 
