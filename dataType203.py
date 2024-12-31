#Python: Check if first digit/character in each element in a given list is same or not
#Write a Python program to check if the first digit or character of each element in a list is the same.
# Define a function 'test' that checks if the first character (or digit) in each element of the given list is the same.
def test(lst):
    # Use a generator expression with 'all' to check if the first character (or digit) of each element matches the first element.
    result = all(str(x)[0] == str(lst[0])[0] for x in lst)
    return result

# Define a list 'nums' containing integers.
nums = [1234, 122, 1984, 19372, 100]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("Check if the first digit in each element of the said given list is the same or not!")
# Call the 'test' function to check if the first digit in each element is the same and print the result.
print(test(nums))

# Define a new list 'nums' with different integer elements.
nums = [1234, 922, 1984, 19372, 100]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the new list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("Check if the first digit in each element of the said given list is the same or not!")
# Call the 'test' function again with the new list 'nums' and print the result.
print(test(nums))

# Define a list 'nums' containing string elements.
nums = ['aabc', 'abc', 'ab', 'a']

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("Check if the first character in each element of the said given list is the same or not!")
# Call the 'test' function to check if the first character in each element is the same and print the result.
print(test(nums))

# Define a new list 'nums' with different string elements.
nums = ['aabc', 'abc', 'ab', 'ha']

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the new list 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("Check if the first character in each element of the said given list is the same or not!")
# Call the 'test' function again with the new list 'nums' and print the result.
print(test(nums)) 
