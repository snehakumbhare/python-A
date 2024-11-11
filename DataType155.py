#Python: Add two given lists of different lengths, start from left

#Write a  Python program to add two given lists of different lengths, starting on the left.
# Define a function called elementswise_left_join that takes two lists, 'l1' and 'l2', as input.
def elementswise_left_join(l1, l2):
    # Calculate the difference in lengths between 'l1' and 'l2' and store it in 'f_len'.
    f_len = len(l1) - (len(l2) - 1)
    
    # Iterate over the indices of 'l2' using a 'for' loop.
    for i in range(0, len(l2), 1):
        # Check if 'f_len - i' is greater than or equal to the length of 'l1'.
        if f_len - i >= len(l1):
            # If the condition is met, exit the loop.
            break
        else:
            # Otherwise, element-wise add the corresponding elements of 'l1' and 'l2'.
            l1[i] = l1[i] + l2[i]
    
    # Return the modified 'l1' list after element-wise left join.
    return l1

# Create two lists, 'nums1' and 'nums2', containing integer values.
nums1 = [2, 4, 7, 0, 5, 8]
nums2 = [3, 3, -1, 7]

# Print a message indicating the original lists.
print("\nOriginal lists:")
print(nums1)
print(nums2)

# Print a message indicating that the two lists are being element-wise left-joined, and call the 'elementswise_left_join' function.
print("\nAdd said two lists from the left:")
print(elementswise_left_join(nums1, nums2))

# Create two lists, 'nums3' and 'nums4', containing integer values.
nums3 = [1, 2, 3, 4, 5, 6]
nums4 = [2, 4, -3]

# Print a message indicating the original lists.
print("\nOriginal lists:")
print(nums3)
print(nums4)

# Print a message indicating that the two lists are being element-wise left-joined, and call the 'elementswise_left_join' function.
print("\nAdd said two lists from the left:")
print(elementswise_left_join(nums3, nums4)) 
