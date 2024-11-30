#Python: Add a number to each element in a given list of numbers

#Write a  Python program to add a number to each element in a given list of numbers.
# Define a function called 'add_val_to_list' that adds a value 'add_val' to each element in a list 'lst'.
def add_val_to_list(lst, add_val):
    # Create a new list 'result' as a reference to the input list 'lst'.
    result = lst
    # Use a list comprehension to add 'add_val' to each element in 'result' and create a new list.
    result = [x + add_val for x in result]
    return result

# Create a list 'nums' containing integer values.
nums = [3, 8, 9, 4, 5, 0, 5, 0, 3]

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Set the value 'add_val' to 3 and print a message indicating the intention to add 'add_val' to each element in the list.
add_val = 3
print("\nAdd", add_val, "to each element in the said list:")

# Call the 'add_val_to_list' function to add 3 to each element in the list 'nums' and print the result.
print(add_val_to_list(nums, add_val))

# Create a list 'nums' containing float values.
nums = [3.2, 8, 9.9, 4.2, 5, 0.1, 5, 3.11, 0]

# Print a message indicating the original list.
print("\nOriginal list:")
print(nums)

# Set the value 'add_val' to 0.51 and print a message indicating the intention to add 'add_val' to each element in the list.
add_val = 0.51
print("\nAdd", add_val, "to each element in the said list:")

# Call the 'add_val_to_list' function to add 0.51 to each element in the list 'nums' and print the result.
print(add_val_to_list(nums, add_val)) 
