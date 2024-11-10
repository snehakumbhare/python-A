#Python: Join two given list of lists of same length, element wise

#Write a  Python program to join two given list of lists of the same length, element wise.

# Define a function called elementswise_join that takes two lists, 'l1' and 'l2', as input.
def elementswise_join(l1, l2):
    # Use a list comprehension to element-wise join the elements of 'l1' and 'l2' using the 'zip' function.
    result = [x + y for x, y in zip(l1, l2)]
    
    # Return the result, which is the element-wise joined list.
    return result

# Create two lists, 'nums1' and 'nums2', containing sublists of varying lengths.
nums1 = [[10, 20], [30, 40], [50, 60], [30, 20, 80]]
nums2 = [[61], [12, 14, 15], [12, 13, 19, 20], [12]]

# Print a message indicating the original lists.
print("Original lists:")
print(nums1)
print(nums2)

# Print a message indicating that the two lists are being element-wise joined, and call the 'elementswise_join' function.
print("\nJoin the said two lists element-wise:")
print(elementswise_join(nums1, nums2))

# Create two lists, 'list1' and 'list2', containing sublists of varying lengths.
list1 = [['a', 'b'], ['b', 'c', 'd'], ['e', 'f']]
list2 = [['p', 'q'], ['p', 's', 't'], ['u', 'v', 'w']]

# Print a message indicating the original lists.
print("\nOriginal lists:")
print(list1)
print(list2)

# Print a message indicating that the two lists are being element-wise joined, and call the 'elementswise_join' function.
print("\nJoin the said two lists element-wise:")
print(elementswise_join(list1, list2)) 
