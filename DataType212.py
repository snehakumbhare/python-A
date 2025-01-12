#Python: Sum of two lowest negative numbers of a given array of integers

#Write a  Python program to calculate the sum of two lowest negative numbers in a given array of integers.

#An integer (from the Latin integer meaning "whole") is colloquially defined as a number that can be written without a fractional component. 
#For example, 21, 4, 0, and −2048 are integers.
# Define a function called 'test' that calculates the sum of the two lowest negative numbers in a list of integers.
def test(nums):
    # Filter the list to include only negative numbers and sort them in ascending order.
    result = sorted([item for item in nums if item < 0])
    # Calculate the sum of the two lowest negative numbers, which are now the first two elements in the sorted list.
    return result[0] + result[1]

# Create a list 'nums' containing a mix of positive and negative integers.
nums = [-14, 15, -10, -11, -12, -13, 16, 17, 18, 19, 20]

# Print a message indicating the original list elements.
print("Original list elements:")
print(nums)

# Calculate and print the sum of the two lowest negative numbers in the list using the 'test' function.
print("Sum of two lowest negative numbers of the said array of integers: ", test(nums))

# Create another list 'nums' with different values.
nums = [-4, 5, -2, 0, 3, -1, 4, 9]

# Print a message indicating the original list elements.
print("\nOriginal list elements:")
print(nums)

# Calculate and print the sum of the two lowest negative numbers in the second list using the 'test' function.
print("Sum of two lowest negative numbers of the said array of integers: ", test(nums))
