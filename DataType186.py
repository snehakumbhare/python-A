#Python: Swap two sublists in a given list

#Write a Python program to swap two sublists in a given list.

# Create a list 'nums' containing integer values from 0 to 15.
nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Print a message indicating the original list.
print("Original list:")
# Print the original list 'nums'.
print(nums)

# Swap two sublists in 'nums'. The sublist from index 6 to 10 is swapped with the sublist from index 1 to 3.
nums[6:10], nums[1:3] = nums[1:3], nums[6:10]

# Print a message indicating that two sublists have been swapped.
print("\nSwap two sublists of the said list:")
# Print the modified 'nums' list with the swapped sublists.
print(nums)

# Swap two sublists in 'nums'. The sublist from index 1 to 3 is swapped with the sublist from index 4 to 6.
nums[1:3], nums[4:6] = nums[4:6], nums[1:3]

# Print a message indicating that two sublists have been swapped again.
print("\nSwap two sublists of the said list:")
# Print the modified 'nums' list with the sublists swapped back to their original positions.
print(nums) 
