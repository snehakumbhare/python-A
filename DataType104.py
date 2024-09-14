#Python: Find the difference between consecutive numbers in a given list

#Write a Python program to find the difference between consecutive numbers in a given list.
# Define a function 'diff_consecutive_nums' that calculates the differences between consecutive numbers in a list
def diff_consecutive_nums(nums):
    # Use a list comprehension and the 'zip' function to calculate differences between consecutive numbers
    result = [b - a for a, b in zip(nums[:-1], nums[1:])]
    return result

# Create a list 'nums1' containing numbers
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums1'
print(nums1)

# Print a message indicating that the differences between consecutive numbers will be determined
print("Difference between consecutive numbers of the said list:")

# Call the 'diff_consecutive_nums' function with 'nums1' and print the result
print(diff_consecutive_nums(nums1))

# Create a list 'nums2' containing numbers
nums2 = [4, 5, 8, 9, 6, 10]

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'nums2'
print(nums2)

# Print a message indicating that the differences between consecutive numbers will be determined
print("Difference between consecutive numbers of the said list:")

# Call the 'diff_consecutive_nums' function with 'nums2' and print the result
print(diff_consecutive_nums(nums2)) 
