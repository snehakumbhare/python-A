#Python: Check whether a specified list is sorted or not
#Write a  Python program to check whether a specified list is sorted or not.
# Define a function 'is_sort_list' that checks if a list is sorted in ascending order
def is_sort_list(nums):
    # Use the 'all' function and a generator expression to check if all elements in the list are in non-decreasing order
    result = all(nums[i] <= nums[i+1] for i in range(len(nums)-1))
    return result

# Create a sorted list 'nums1' with integers
nums1 = [1,2,4,6,8,10,12,14,16,17]

# Print a message indicating the original list
print ("Original list:")
# Print the contents of the 'nums1' list
print(nums1)

# Print a message indicating whether the list is sorted
print("\nIs the said list is sorted!")

# Call the 'is_sort_list' function with 'nums1' and print the result
print(is_sort_list(nums1))

# Create an unsorted list 'nums2' with integers
nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]

# Print a message indicating the original list
print ("\nOriginal list:")
# Print the contents of the 'nums2' list (Note: There's a typo here; it should be 'nums2' instead of 'nums1')
print(nums2)

# Print a message indicating whether the list is sorted
print("\nIs the said list is sorted!")

# Call the 'is_sort_list' function with 'nums2' and print the result
print(is_sort_list(nums2))
