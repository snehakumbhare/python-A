#Python: Compare two given lists and find the indices of the values present in both lists

#Write a  Python program to compare two given lists and find the indices of the values present in both lists.
# Define a function 'matched_index' that finds the indices of values in 'l1' that are also present in 'l2'.
def matched_index(l1, l2):
    # Convert 'l2' into a set for faster membership checking.
    l2 = set(l2)
    # Use list comprehension to find the indices of elements in 'l1' that are also in 'l2'.
    return [i for i, el in enumerate(l1) if el in l2]

# Create two lists 'nums1' and 'nums2'.
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 5, 2, 10, 12]

# Print a message indicating the original lists.
print("Original lists:")
# Print both 'nums1' and 'nums2'.
print(nums1)
print(nums2)

# Print a message indicating the purpose of the following line of code.
print("Compare said two lists and get the indices of the values present in both lists:")
# Call the 'matched_index' function to find the indices of values present in both 'nums1' and 'nums2'.
print(matched_index(nums1, nums2))

# Update 'nums1' and 'nums2' with new values.
nums1 = [1, 2, 3, 4, 5, 6]
nums2 = [7, 8, 5, 7, 10, 12]

# Print a message indicating the updated original lists.
print("\nOriginal lists:")
# Print both updated 'nums1' and 'nums2'.
print(nums1)
print(nums2)

# Print a message indicating the purpose of the following line of code.
print("Compare said two lists and get the indices of the values present in both lists:")
# Call the 'matched_index' function to find the indices of values present in both updated 'nums1' and 'nums2'.
print(matched_index(nums1, nums2))

# Update 'nums1' and 'nums2' with different values.
nums1 = [1, 2, 3, 4, 15, 6]
nums2 = [7, 8, 5, 7, 10, 12]

# Print a message indicating the updated original lists.
print("\nOriginal lists:")
# Print both updated 'nums1' and 'nums2'.
print(nums1)
print(nums2)

# Print a message indicating the purpose of the following line of code.
print("Compare said two lists and get the indices of the values present in both lists:")
# Call the 'matched_index' function to find the indices of values present in both updated 'nums1' and 'nums2'.
print(matched_index(nums1, nums2)) 
