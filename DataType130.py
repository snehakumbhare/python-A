#Python: Count the same pair in three given lists

#Write a Python program to count the same pair in three given lists.
# Define a function 'count_same_pair' that counts the number of same pairs between three lists
def count_same_pair(nums1, nums2, nums3):
    # Use a generator expression within the 'sum' function to count the same pairs
    result = sum(m == n == o for m, n, o in zip(nums1, nums2, nums3))
    return result

# Create three lists 'nums1', 'nums2', and 'nums3'
nums1 = [1, 2, 3, 4, 5, 6, 7, 8]
nums2 = [2, 2, 3, 1, 2, 6, 7, 9]
nums3 = [2, 1, 3, 1, 2, 6, 7, 9]

# Print a message indicating the original lists
print("Original lists:")
# Print the contents of 'nums1', 'nums2', and 'nums3'
print(nums1)
print(nums2)
print(nums3)

# Print a message indicating the operation to count same pairs
print("\nNumber of same pairs in the said three given lists:")
# Call the 'count_same_pair' function with 'nums1', 'nums2', and 'nums3' and print the result
print(count_same_pair(nums1, nums2, nums3)) 
