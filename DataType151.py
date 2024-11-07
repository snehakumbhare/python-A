#Python: Find the maximum and minimum values in a given list within specified index range
#Write a  Python program to find the maximum and minimum values in a given list within a specified index range.
# Define a function called reverse_list_of_lists that takes three arguments: nums, lr, and hr.
def reverse_list_of_lists(nums, lr, hr):
    # Create an empty list called temp to store elements within the specified index range.
    temp = []
    
    # Iterate over the elements and their indices in the 'nums' list.
    for idx, el in enumerate(nums):
        # Check if the current index is greater than or equal to 'lr' and less than 'hr'.
        if idx >= lr and idx < hr:
            # If the condition is met, append the element 'el' to the 'temp' list.
            temp.append(el)
    
    # Calculate the maximum value of the elements in the 'temp' list.
    result_max = max(temp)
    
    # Calculate the minimum value of the elements in the 'temp' list.
    result_min = min(temp)
    
    # Return the maximum and minimum values found within the specified index range.
    return result_max, result_min

# Create a list 'nums' containing some values.
nums = [4, 3, 0, 5, 3, 0, 2, 3, 4, 2, 4, 3, 5]

# Print the original list.
print("Original list:")
print(nums)

# Print the specified index range.
lr = 3
hr = 8
print("\nIndex range:")
print(lr, "to", hr)

# Print the maximum and minimum values of the 'nums' list within the specified index range.
print("\nMaximum and minimum values of the said given list within the index range:")
print(reverse_list_of_lists(nums, lr, hr))
