#Python: Compute average of two given lists

#Write a  Python program to compute average of two given lists.
# Define a function 'average_two_lists' that calculates the average of two lists
def average_two_lists(nums1, nums2):
    # Calculate the average by summing the elements of both lists and dividing by their combined length
    result = sum(nums1 + nums2) / len(nums1 + nums2)
    return result

# Create two lists 'nums1' and 'nums2' containing numbers
nums1 = [1, 1, 3, 4, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 4, 5, 7, 8]

# Print a message indicating the original lists
print("Original list:")
# Print the contents of 'nums1' and 'nums2'
print(nums1)
print(nums2)

# Print a message indicating that the average of the two lists will be calculated
print("\nAverage of two lists:")

# Call the 'average_two_lists' function with 'nums1' and 'nums2' and print the result
print(average_two_lists(nums1, nums2))
