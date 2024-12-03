#Python: Create a new list dividing two given lists of numbers

#Write a Python program to create a new list by dividing two given lists of numbers.
# Define a function called 'dividing_two_lists' that divides each element of two lists 'l1' and 'l2' element-wise.
def dividing_two_lists(l1, l2):
    # Use 'zip' to pair elements from 'l1' and 'l2', then use a list comprehension to divide each pair (x, y) and create a new list 'result'.
    result = [x / y for x, y in zip(l1, l2)]
    return result

# Create two lists of numbers 'nums1' and 'nums2'.
nums1 = [7, 2, 3, 4, 9, 2, 3]
nums2 = [9, 8, 2, 3, 3, 1, 2]

# Print a message indicating the original lists.
print("Original lists:")
print(nums1)
print(nums2)

# Call the 'dividing_two_lists' function to divide the elements of 'nums1' by the corresponding elements of 'nums2' and print the result.
print(dividing_two_lists(nums1, nums2)) 
