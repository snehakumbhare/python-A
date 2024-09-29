#Python: Find the difference between elements (n+1th – nth) of a given list of numeric values
#Write a  Python program to find the difference between elements (n+1th – nth) of a given list of numeric values.
# Define a function 'elements_difference' that calculates the differences between adjacent elements in a list
def elements_difference(nums):
    # Use a list comprehension with zip to calculate differences (n+1th – nth)
    result = [j - i for i, j in zip(nums[:-1], nums[1:])]
    return result

# Create two lists 'nums1' and 'nums2'
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
nums2 = [2, 4, 6, 8]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums1'
print(nums1)
# Print a message indicating the operation to calculate differences
print("\nDifference between elements (n+1th – nth) of the said list:")
# Call the 'elements_difference' function with 'nums1' and print the result
print(elements_difference(nums1))

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'nums2'
print(nums2)
# Print a message indicating the operation to calculate differences
print("\nDifference between elements (n+1th – nth) of the said list:")
# Call the 'elements_difference' function with 'nums2' and print the result
print(elements_difference(nums2)) 
