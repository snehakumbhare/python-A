#Python: Find the difference between two list including duplicate elements

#Write a  Python program to find the difference between two lists including duplicate elements.

# Define a function 'list_difference' that finds the difference between two lists (including duplicate elements)
def list_difference(l1, l2):
    # Create a copy of 'l1' to avoid modifying the original list
    result = list(l1)
    
    # Iterate through elements in 'l2'
    for el in l2:
        # Remove the first occurrence of 'el' from 'result'
        result.remove(el)
    
    # Return the modified 'result' list containing the difference
    return result

# Create two lists 'l1' and 'l2' with duplicate elements
l1 = [1, 1, 2, 3, 3, 4, 4, 5, 6, 7]
l2 = [1, 1, 2, 4, 5, 6]

# Print a message indicating the original lists
print("Original lists:")
# Print the contents of 'l1' and 'l2'
print(l1)
print(l2)

# Find the difference between 'l1' and 'l2' (including duplicate elements)
print("\nDifference between two said lists (including duplicate elements):")
# Call the 'list_difference' function with 'l1' and 'l2', then print the result
print(list_difference(l1, l2))
