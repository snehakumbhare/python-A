#Python: Interleave two given list into another list randomly

#Write a Python program to combine two lists into another list randomly.

# Import the 'random' module to generate random values
import random

# Define a function 'randomly_interleave' that interleaves two lists randomly
def randomly_interleave(nums1, nums2):
    # Create a new list by sampling elements from 'nums1' and 'nums2'
    # The elements from 'nums1' and 'nums2' are interleaved randomly
    result = [x.pop(0) for x in random.sample([nums1] * len(nums1) + [nums2] * len(nums2), len(nums1) + len(nums2))]
    return result

# Create two lists 'nums1' and 'nums2'
nums1 = [1, 2, 7, 8, 3, 7]
nums2 = [4, 3, 8, 9, 4, 3, 8, 9]

# Print a message indicating the original lists
print("Original lists:")
# Print the contents of 'nums1' and 'nums2'
print(nums1)
print(nums2)

# Print a message indicating the operation to interleave the two lists
print("\nInterleave two given lists into another list randomly:")
# Call the 'randomly_interleave' function with 'nums1' and 'nums2', then print the result
print(randomly_interleave(nums1, nums2))
