#Python: Access multiple elements of specified index from a given list

#Write a  Python program to access multiple elements at a specified index from a given list.
# Define a function 'access_elements' that extracts elements from a list based on their indices
def access_elements(nums, list_index):
    # Use list comprehension to create a new list containing elements from 'nums' at the specified indices in 'list_index'
    result = [nums[i] for i in list_index]
    return result

# Create a list 'nums' with integers
nums = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]

# Print a message indicating the original list
print ("Original list:")
# Print the contents of the 'nums' list
print(nums)

# Create a list 'list_index' containing indices
list_index = [0,3,5,7,10]

# Print a message indicating the index list
print("Index list:")
# Print the contents of the 'list_index' list
print(list_index)

# Print a message indicating the items with specified indices in the list
print("\nItems with specified index of the said list:")
# Call the 'access_elements' function with 'nums' and 'list_index', and print the result
print(access_elements(nums, list_index)) 
