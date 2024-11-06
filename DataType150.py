#Python: Reverse a given list of lists

#Write a  Python program to reverse a given list of lists.
# Define a function called reverse_list_of_lists that takes a single argument 'list1'.
def reverse_list_of_lists(list1):
    # Use slicing to reverse the order of the elements in the 'list1'.
    return list1[::-1]

# Create a list 'colors' containing sublists.
colors = [['orange', 'red'], ['green', 'blue'], ['white', 'black', 'pink']]

# Print the original list.
print("Original list:")
print(colors)

# Print a message indicating that the list of lists is being reversed.
print("\nReverse said list of lists:")

# Call the 'reverse_list_of_lists' function to reverse the 'colors' list and print the result.
print(reverse_list_of_lists(colors))

# Create a list 'nums' containing sublists with different lengths.
nums = [[1, 2, 3, 4], [0, 2, 4, 5], [2, 3, 4, 2, 4]]

# Print a message indicating that the original list is being displayed.
print("\nOriginal list:")
print(nums)

# Print a message indicating that the list of lists is being reversed.
print("\nReverse said list of lists:")

# Call the 'reverse_list_of_lists' function to reverse the 'nums' list and print the result.
print(reverse_list_of_lists(nums))
