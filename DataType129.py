#Python: Reverse each list in a given list of lists

#Write a  Python program to reverse each list in a given list of lists.

# Define a function 'reverse_list_lists' that reverses each list within a list of lists
def reverse_list_lists(nums):
    # Iterate through each sublist 'l' in the 'nums' list
    for l in nums:
        # Sort each sublist 'l' in reverse order
        l.sort(reverse=True)
    return nums

# Create a list of lists 'nums'
nums = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

# Print a message indicating the original list of lists
print("Original list of lists:")
print(nums)

# Print a message indicating the operation to reverse each list
print("\nReverse each list in the said list of lists:")
# Call the 'reverse_list_lists' function with 'nums' and print the result
print(reverse_list_lists(nums))
