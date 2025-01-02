#Python: Find the indices of elements of a given list, greater than a specified value

#Write a  Python program to find the indices of elements in a given list that are greater than a specified value.

# Define a function 'test' that finds the indices of elements in the given list that are greater than a specified value.
def test(lst, value):
    # Use a list comprehension with 'enumerate' to find the indices of elements that are greater than 'value'.
    result = [i for i, val in enumerate(lst) if val > value]
    return result

# Define a list 'nums' containing integers.
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list 'nums'.
print(nums)

# Set a value 'val'.
val = 3000

# Print a message indicating the purpose of the following lines of code.
print("Indices of elements of the said list, greater than", val)
# Call the 'test' function to find indices of elements greater than 'val' and print the result.
print(test(nums, val))

# Define a new list 'nums' with the same integer elements.
nums = [1234, 1522, 1984, 19372, 1000, 2342, 7626]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the new list 'nums'.
print(nums)

# Set a new value 'val'.
val = 20000

# Print a message indicating the purpose of the following lines of code.
print("Indices of elements of the said list, greater than", val)
# Call the 'test' function again with the new value 'val' and print the result.
print(test(nums, val))
