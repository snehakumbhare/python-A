#Python: Extract specified number of elements from a given list, which follows each other continuously

#Write a  Python program to extract specified number of elements from a given list,
#which follows each other continuously.

# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

# Define a function 'extract_elements' that extracts elements from a list that follow each other continuously and occur 'n' times
def extract_elements(nums, n):
    # Use a list comprehension and 'groupby' to filter elements in 'nums' that occur 'n' times in a row
    result = [i for i, j in groupby(nums) if len(list(j)) == n]
    return result

# Create a list 'nums1' containing numbers
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]

# Set the value of 'n' to 2
n = 2

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums1'
print(nums1)

# Print a message indicating the number of elements to extract and the criteria for extraction
print("Extract 2 number of elements from the said list which follows each other continuously:")

# Call the 'extract_elements' function with 'nums1' and 'n', then print the result
print(extract_elements(nums1, n))

# Create a list 'nums2' containing numbers
nums2 = [0, 1, 2, 3, 4, 4, 4, 4, 5, 7]

# Set the value of 'n' to 4
n = 4

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums2'
print(nums2)

# Print a message indicating the number of elements to extract and the criteria for extraction
print("Extract 4 number of elements from the said list which follows each other continuously:")

# Call the 'extract_elements' function with 'nums2' and 'n', then print the result
print(extract_elements(nums2, n))
