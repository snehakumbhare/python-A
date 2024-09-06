#Python: Remove sublists from a given list of lists, which are outside a given range
#Write a Python program to remove sublists from a given list of lists that contain an element outside a given range.
# Define a function 'remove_list_range' that removes sublists from 'input_list' based on specified range criteria
# Source: bit.ly/33MAeHe
def remove_list_range(input_list, left_range, right_range):
    # Use a list comprehension to filter sublists that meet the range criteria
    result = [i for i in input_list if (min(i) >= left_range and max(i) <= right_range)]
    return result

# Create a list 'list1' containing sublists of numbers
list1 = [[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]

# Define left and right range values
left_range = 13
right_range = 17

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the sublists that contain elements outside the given range will be removed
print("\nAfter removing sublists from a given list of lists, which contains an element outside the given range:")

# Call the 'remove_list_range' function with 'list1' and the specified range, then print the result
print(remove_list_range(list1, left_range, right_range))
