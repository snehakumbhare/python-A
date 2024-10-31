#Python: Compute the sum of digits of each number of a given list

#Write a  Python program to compute the sum of digits of each number in a given list.

# Define a function 'sum_of_digits' that calculates the sum of digits in a list of integers
def sum_of_digits(nums):
    # Use a nested generator expression to iterate over elements in 'nums'
    # Convert each element to a string and iterate over its characters
    # Use 'isdigit()' to check if a character is a digit, convert it to an integer, and sum them
    return sum(int(el) for n in nums for el in str(n) if el.isdigit())

# Create a list of integers 'nums'
nums = [10, 2, 56]

# Print a message indicating the original list
print("Original tuple:")
print(nums)

# Print a message indicating the operation to calculate the sum of digits in the list
print("Sum of digits of each number of the said list of integers:")
# Call the 'sum_of_digits' function with 'nums' and print the result
print(sum_of_digits(nums))

# Create another list with a mix of integers and non-integer values
nums = [10, 20, 4, 5, 'b', 70, 'a']

# Print a message indicating the original list
print("\nOriginal tuple:")
print(nums)

# Print a message indicating the operation to calculate the sum of digits in the list
print("Sum of digits of each number of the said list of integers:")
# Call the 'sum_of_digits' function with 'nums' and print the result
print(sum_of_digits(nums))

# Create a list of integers, including negative values
nums = [10, 20, -4, 5, -70]

# Print a message indicating the original list
print("\nOriginal tuple:")
print(nums)

# Print a message indicating the operation to calculate the sum of digits in the list
print("Sum of digits of each number of the said list of integers:")
# Call the 'sum_of_digits' function with 'nums' and print the result
print(sum_of_digits(nums))
