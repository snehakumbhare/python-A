#Python: Interleave multiple lists of different lengths
#Write a  Python program to interleave lists of varying lengths.
# Define a function called interleave_diff_len_lists that takes four lists as input: 'list1', 'list2', 'list3', and 'list4'.
def interleave_diff_len_lists(list1, list2, list3, list4):
    # Create an empty list called 'result' to store the interleaved elements.
    result = []
    
    # Get the lengths of the input lists and store them in 'l1', 'l2', 'l3', and 'l4'.
    l1 = len(list1)
    l2 = len(list2)
    l3 = len(list3)
    l4 = len(list4)
    
    # Iterate from 0 to the maximum length among the input lists using 'max' function.
    for i in range(max(l1, l2, l3, l4)):
        # Check if 'i' is less than 'l1' and add the element from 'list1' to 'result'.
        if i < l1:
            result.append(list1[i])
        # Check if 'i' is less than 'l2' and add the element from 'list2' to 'result'.
        if i < l2:
            result.append(list2[i])
        # Check if 'i' is less than 'l3' and add the element from 'list3' to 'result'.
        if i < l3:
            result.append(list3[i])
        # Check if 'i' is less than 'l4' and add the element from 'list4' to 'result'.
        if i < l4:
            result.append(list4[i])
    
    # Return the 'result' list containing interleaved elements from the input lists.
    return result

# Create four lists of different lengths: 'nums1', 'nums2', 'nums3', and 'nums4'.
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [2, 5, 8]
nums3 = [0, 1]
nums4 = [3, 3, -1, 7]

# Print a message indicating the original lists.
print("\nOriginal lists:")
print(nums1)
print(nums2)
print(nums3)
print(nums4)

# Print a message indicating that the lists are being interleaved, and call the 'interleave_diff_len_lists' function.
print("\nInterleave said lists of different lengths:")
print(interleave_diff_len_lists(nums1, nums2, nums3, nums4)) 
