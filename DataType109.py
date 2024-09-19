#Python: Rotate a given list by specified number of items to the right or left direction
#Write a  Python program to rotate a given list by a specified number of items in the right or left direction.
# Create a list 'nums1' with integers from 1 to 10
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Print a message indicating the original list
print("Original List:")
# Print the contents of 'nums1'
print(nums1)

# Print a message indicating that the list will be rotated to the left by 4 positions
print("\nRotate the said list in left direction by 4:")
# Perform a left rotation by slicing the list
result = nums1[3:] + nums1[:4]
# Print the rotated list
print(result)

# Print a message indicating that the list will be rotated to the left by 2 positions
print("\nRotate the said list in left direction by 2:")
# Perform a left rotation by slicing the list
result = nums1[2:] + nums1[:2]
# Print the rotated list
print(result)

# Print a message indicating that the list will be rotated to the right by 4 positions
print("\nRotate the said list in Right direction by 4:")
# Perform a right rotation by slicing the list
result = nums1[-3:] + nums1[:-4]
# Print the rotated list
print(result)

# Print a message indicating that the list will be rotated to the right by 2 positions
print("\nRotate the said list in Right direction by 2:")
# Perform a right rotation by slicing the list
result = nums1[-2:] + nums1[:-2]
# Print the rotated list
print(result)
