#Python: Remove the specific item from a given list of lists
#Write a Python program to remove a specific item from a given list of lists.
# Import the 'copy' module
import copy	

# Define a function 'remove_list_of_lists' that removes elements at a specified index from sublists
def remove_list_of_lists(color, N):
    # Loop through each sublist in 'color'
    for x in color:
        # Remove the element at index 'N' from the current sublist
        del x[N]
    return color

# Create a list of lists 'nums' containing color-related data
nums = [
        ["Red", "Maroon", "Yellow", "Olive"],
        ["#FF0000", "#800000", "#FFFF00", "#808000"],
        ["rgb(255,0,0)", "rgb(128,0,0)", "rgb(255,255,0)", "rgb(128,128,0)"]
       ]

# Create deep copies of the original list 'nums'
nums1 = copy.deepcopy(nums)
nums2 = copy.deepcopy(nums)
nums3 = copy.deepcopy(nums)

# Print a message indicating the original list of lists
print("Original list of lists:")
# Print the contents of 'nums'
print(nums)

# Set 'N' to 0 (to remove the 1st item)
N = 0
# Print a message indicating the removal of the 1st item
print("\nRemove 1st item from the said list of lists:")
# Call the 'remove_list_of_lists' function with 'nums1' and 'N', then print the result
print(remove_list_of_lists(nums1, N))

# Set 'N' to 1 (to remove the 2nd item)
N = 1
# Print a message indicating the removal of the 2nd item
print("\nRemove 2nd item from the said list of lists:")
# Call the 'remove_list_of_lists' function with 'nums2' and 'N', then print the result
print(remove_list_of_lists(nums2, N))

# Set 'N' to 3 (to remove the 4th item)
N = 3
# Print a message indicating the removal of the 4th item
print("\nRemove 4th item from the said list of lists:")
# Call the 'remove_list_of_lists' function with 'nums3' and 'N', then print the result
print(remove_list_of_lists(nums3, N))

