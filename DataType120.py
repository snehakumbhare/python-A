#Python: Create a list taking alternate elements from a given list

#Write a  Python program to create a list taking alternate elements from a given list.

# Define a function 'alternate_elements' that returns a list of alternate elements from the input list
def alternate_elements(list_data):
    # Initialize an empty list 'result' to store the alternate elements
    result = []
    # Use a for loop to iterate over elements in 'list_data' with a step of 2 (alternate elements)
    for item in list_data[::2]:
        # Append the alternate element to the 'result' list
        result.append(item)
    # Return the 'result' list containing alternate elements
    return result

# Create a list 'colors' with string values
colors = ["red", "black", "white", "green", "orange"]
# Print a message indicating the original list
print("Original list:")
# Print the contents of 'colors'
print(colors)
# Print a message indicating the operation to extract alternate elements
print("List with alternate elements from the said list:")
# Call the 'alternate_elements' function with 'colors' and print the result
print(alternate_elements(colors))

# Create a list 'nums' with integer values
nums = [2, 0, 3, 4, 0, 2, 8, 3, 4, 2]
# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'nums'
print(nums)
# Print a message indicating the operation to extract alternate elements
print("List with alternate elements from the said list:")
# Call the 'alternate_elements' function with 'nums' and print the result
print(alternate_elements(nums))
