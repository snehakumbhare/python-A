#Python: Maximum and minimum value of the three given lists

#Write a  Python program to find the maximum and minimum values of the three given lists.
# Create three lists 'nums1', 'nums2', and 'nums3' containing integers.
nums1 = [2, 3, 5, 8, 7, 2, 3]
nums2 = [4, 3, 9, 0, 4, 3, 9]
nums3 = [2, 1, 5, 6, 5, 5, 4]

# Print a message indicating the original lists.
print("Original lists:")
# Print each of the three lists 'nums1', 'nums2', and 'nums3'.
print(nums1)
print(nums2)
print(nums3)

# Print a message indicating the maximum value of the three lists.
print("Maximum value of the said three lists:")
# Calculate the maximum value by combining all three lists and using the 'max' function.
print(max(nums1 + nums2 + nums3))

# Print a message indicating the minimum value of the three lists.
print("Minimum value of the said three lists:")
# Calculate the minimum value by combining all three lists and using the 'min' function.
print(min(nums1 + nums2 + nums3))
