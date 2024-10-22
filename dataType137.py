#Python: First even and odd number in a given list of numbers

#Write a  Python program to find the first even and odd number in a given list of numbers.
# Define a function 'first_even_odd' that finds the first even and odd numbers in a list
def first_even_odd(nums):
    # Use 'next' to find the first even number, default to -1 if not found
    first_even = next((el for el in nums if el % 2 == 0), -1)
    # Use 'next' to find the first odd number, default to -1 if not found
    first_odd = next((el for el in nums if el % 2 != 0), -1)
    return first_even, first_odd

# Create a list of numbers 'nums'
nums = [1, 3, 5, 7, 4, 1, 6, 8]

# Print a message indicating the original list of numbers
print("Original list:")
# Print the contents of 'nums'
print(nums)

# Find the first even and odd numbers in the list using the 'first_even_odd' function
print("\nFirst even and odd number of the said list of numbers:")
# Call the 'first_even_odd' function with 'nums', then print the result
print(first_even_odd(nums)) 
