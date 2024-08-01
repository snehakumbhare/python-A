#Python: Move all zero digits to end of a given list of numbers
#Write a  Python program to move all zero digits to the end of a given list of numbers.
# Define a function 'test' that takes a list 'lst' as an argument
def test(lst):
    # Sort the list 'lst' based on the key provided by the lambda function
    # The key function returns 'True' for non-zero elements and 'False' for zero elements
    result = sorted(lst, key=lambda x: not x) 
    return result

# Define a list 'nums' containing integers
nums = [3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]

# Print the original list 'nums'
print("\nOriginal list:")
print(nums)

# Print a message indicating the purpose of the following output
print("\nMove all zero digits to the end of the said list of numbers:")

# Call the 'test' function with 'nums' as an argument and print the result
# This will move all zero digits to the end of the list
print(test(nums))
