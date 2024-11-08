#Python: Combine two given sorted lists using heapq module

#Write a  Python program to combine two sorted lists using the heapq module.

# Import the 'merge' function from the 'heapq' module, which is used to merge two sorted lists.
from heapq import merge

# Create two sorted lists 'nums1' and 'nums2'.
nums1 = [1, 3, 5, 7, 9, 11]
nums2 = [0, 2, 4, 6, 8, 10]

# Print a message indicating the original sorted lists.
print("Original sorted lists:")
print(nums1)
print(nums2)

# Print a message indicating that the two sorted lists are being merged.

print("\nAfter merging the said two sorted lists:")
# Use the 'merge' function to merge the two sorted lists, convert the result to a list, and print it.
print(list(merge(nums1, nums2))) 

