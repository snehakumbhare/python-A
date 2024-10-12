#Python: Sum of the numbers in a list between the indices of a specified range
#Write a  Python program to calculate the sum of the numbers in a list between the indices of a specified range.
# Define a function 'sum_Range_list' that calculates the sum of a specified range within a list
def sum_Range_list(nums, m, n):
    # Initialize 'sum_range' to store the sum of the specified range
    sum_range = 0
    
    # Iterate through the list from index 'm' to 'n'
    for i in range(m, n+1, 1):
        # Add the value at the current index 'i' to 'sum_range'
        sum_range += nums[i]
    
    return sum_range

# Create a list of numbers 'nums'
nums = [2, 1, 5, 6, 8, 3, 4, 9, 10, 11, 8, 12]

# Print a message indicating the original list
print("Original list:")
print(nums)

# Set the range boundaries 'm' and 'n'
m = 8
n = 10

# Print a message indicating the specified range
print("Range:", m, ",", n)

# Print a message indicating the sum of the specified range
print("\nSum of the specified range:")
# Call the 'sum_Range_list' function with 'nums', 'm', and 'n', then print the result
print(sum_Range_list(nums, m, n))  
