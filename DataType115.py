#Python: Check if the elements of a given list are unique or not

#Write a Python program to check if the elements of a given list are unique or not.
# Define a function 'all_unique' that checks if all elements in a list are unique
def all_unique(test_list):
    # Check if the length of the list is greater than the length of the set of the list
    if len(test_list) > len(set(test_list)):
        return False
    return True

# Create a list 'nums1' with duplicate elements
nums1 = [1, 2, 4, 6, 8, 2, 1, 4, 10, 12, 14, 12, 16, 17]
# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums1'
print(nums1)

# Print a message indicating the check for unique elements in the list
print("\nIs the said list contains all unique elements!")
# Call the 'all_unique' function with 'nums1' and print the result
print(all_unique(nums1)) 

# Create a list 'nums2' with unique elements
nums2 = [2, 4, 6, 8, 10, 12, 14]
# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'nums2'
print(nums2)

# Print a message indicating the check for unique elements in the list
print("\nIs the said list contains all unique elements!")
# Call the 'all_unique' function with 'nums2' and print the result
print(all_unique(nums2))
