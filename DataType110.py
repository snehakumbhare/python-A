#Python: Find the item with maximum occurrences in a given list

#Write a  Python program to find the item with the most occurrences in a given list.
# Define a function 'max_occurrences' that finds the item with the maximum occurrences in a list
def max_occurrences(nums):
    # Initialize 'max_val' to 0 and 'result' to the first item in the list
    max_val = 0
    result = nums[0]
    
    # Iterate through the elements in the 'nums' list
    for i in nums:
        # Count the occurrences of the current element 'i' in the list
        occu = nums.count(i)
        
        # Check if the number of occurrences is greater than the current maximum
        if occu > max_val:
            # Update 'max_val' and 'result' if a higher occurrence is found
            max_val = occu
            result = i
    
    # Return the item with the maximum occurrences
    return result

# Create a list 'nums' with integers
nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]

# Print a message indicating the original list
print ("Original list:")
# Print the contents of the 'nums' list
print(nums)

# Print a message indicating the item with the maximum occurrences in the list
print("\nItem with maximum occurrences of the said list:")
# Call the 'max_occurrences' function with 'nums' and print the result
print(max_occurrences(nums)) 
