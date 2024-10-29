#Python: Extract every first or specified element from a given two-dimensional list

#Write a Python program to extract every first or specified element from a given two-dimensional list.

# Define a function 'specified_element' that extracts elements at a specified index from a list of lists
def specified_element(nums, N):
    # Use a list comprehension to extract the element at index 'N' from each sub-list
    result = [i[N] for i in nums]
    return result

# Create a list of lists 'nums' representing a 2D matrix
nums = [
        [1, 2, 3, 2],
        [4, 5, 6, 2],
        [7, 1, 9, 5],
       ]

# Print a message indicating the original list of lists
print("Original list of lists:")
# Print the contents of 'nums'
print(nums)

# Set the index 'N' to 0
N = 0
# Print a message indicating the operation to extract every first element
print("\nExtract every first element from the said given two-dimensional list:")
# Call the 'specified_element' function with 'nums' and index 'N', then print the result
print(specified_element(nums, N))

# Set the index 'N' to 2
N = 2
# Print a message indicating the operation to extract every third element
print("\nExtract every third element from the said given two-dimensional list:")
# Call the 'specified_element' function with 'nums' and index 'N', then print the result
print(specified_element(nums, N)) 
