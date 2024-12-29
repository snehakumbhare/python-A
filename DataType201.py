#Python: Find the indexes of all None items in a given list

#Write a  Python program to find the indexes of all None items in a given list.

# Define a function 'relative_order' that finds the indexes of all None items in a list.
def relative_order(lst):
    # Use a list comprehension to iterate over the indexes 'i' and elements in the list 'lst'.
    # For each element, check if it is equal to None, and if it is, include its index 'i' in the result list.
    result = [i for i in range(len(lst)) if lst[i] == None]
    # Return the list of indexes of None items.
    return result

# Define a list 'nums' containing various elements, including None values.
nums = [1, None, 5, 4, None, 0, None, None]

# Print a message indicating the original list.
print("Original list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nIndexes of all None items of the list:")
# Call the 'relative_order' function to find the indexes of all None items in the list 'nums'.
print(relative_order(nums))
