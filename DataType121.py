#Python: Find the nested lists elements which are present in another list

#Write a Python program to find nested list elements that are present in another list.
# Define a function 'intersection_nested_lists' that finds the intersection of elements between two nested lists
def intersection_nested_lists(l1, l2):
    # Use a list comprehension to iterate over 'l2', filtering elements that are present in 'l1'
    result = [[n for n in lst if n in l1] for lst in l2]
    # Return the 'result' list containing the intersections
    return result

# Create a list 'nums1' with integer values
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
# Create a nested list 'nums2' with sublists containing integer values
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# Print a message indicating the original lists
print("\nOriginal lists:")
# Print the contents of 'nums1'
print(nums1)
# Print the contents of 'nums2'
print(nums2)
# Print a message indicating the operation to find the intersection of nested lists
print("\nIntersection of said nested lists:")
# Call the 'intersection_nested_lists' function with 'nums1' and 'nums2', then print the result
print(intersection_nested_lists(nums1, nums2))
