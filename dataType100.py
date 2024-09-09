#Python: Common index elements from more than one list
#Write a  Python program to extract common index elements from more than one given list.
# Define a function 'extract_index_ele' that finds common elements at the same index in three lists
def extract_index_ele(l1, l2, l3):
    result = []
    # Use the 'zip' function to iterate through elements at the same index in the three lists
    for m, n, o in zip(l1, l2, l3):
        # If the elements at the current index in all three lists are equal, append it to 'result'
        if (m == n == o):
            result.append(m)
    return result

# Create three lists 'nums1', 'nums2', and 'nums3' containing numbers
nums1 = [1, 1, 3, 4, 5, 6, 7]
nums2 = [0, 1, 2, 3, 4, 5, 7]
nums3 = [0, 1, 2, 3, 4, 5, 7]

# Print a message indicating the original lists
print("Original lists:")
# Print the contents of 'nums1'
print(nums1)
# Print the contents of 'nums2'
print(nums2)
# Print the contents of 'nums3'
print(nums3)

# Print a message indicating the common elements at the same index in the lists will be determined
print("\nCommon index elements of the said lists:")

# Call the 'extract_index_ele' function with 'nums1', 'nums2', and 'nums3' and print the result
print(extract_index_ele(nums1, nums2, nums3)) 
