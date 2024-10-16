#Python: Find all index positions of the maximum and minimum values in a given list
#Write a  Python program to find all index positions of the maximum and minimum values in a given list of numbers.
# Define a function 'position_max_min' that finds the index positions of the maximum and minimum values in a list
def position_max_min(nums):
    # Find the maximum and minimum values in the 'nums' list
    max_val = max(nums)
    min_val = min(nums)

    # Create a list 'max_result' with the index positions of the maximum value in 'nums'
    max_result = [i for i, j in enumerate(nums) if j == max_val]

    # Create a list 'min_result' with the index positions of the minimum value in 'nums'
    min_result = [i for i, j in enumerate(nums) if j == min_val]

    # Return both 'max_result' and 'min_result'
    return max_result, min_result

# Create a list 'nums' with numeric values
nums = [12, 33, 23, 10, 67, 89, 45, 667, 23, 12, 11, 10, 54]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums'
print(nums)

# Call the 'position_max_min' function with 'nums' and store the result in 'result'
result = position_max_min(nums)

# Print a message indicating the index positions of the maximum value in the list
print("\nIndex positions of the maximum value of the said list:")
# Print the index positions of the maximum value from 'result'
print(result[0])

# Print a message indicating the index positions of the minimum value in the list
print("\nIndex positions of the minimum value of the said list:")
# Print the index positions of the minimum value from 'result'
print(result[1]) 
