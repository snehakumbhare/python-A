#Python: Join adjacent members of a given list

#Write a  Python program to join adjacent members of a given list.
# Define a function 'test' that joins adjacent members of a given list.
def test(lst):
    # Use list comprehensions to iterate over the list, taking elements at even and odd positions.
    # Add the adjacent elements together and store the results in the 'result' list.
    result = [x + y for x, y in zip(lst[::2], lst[1::2])]
    # Return the 'result' list with joined adjacent members.
    return result

# Define a list 'nums' containing string elements.
nums = ['1', '2', '3', '4', '5', '6', '7', '8']

# Print a message indicating the original list.
print("Original list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nJoin adjacent members of a given list:")
# Call the 'test' function to join adjacent members of the list 'nums' and print the result.
print(test(nums))

# Define a new list 'nums' with fewer elements.
nums = ['1', '2', '3']

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the new list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nJoin adjacent members of a given list:")
# Call the 'test' function again with the new list 'nums' and print the result.
print(test(nums))
