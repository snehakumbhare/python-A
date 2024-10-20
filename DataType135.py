#Python: Iterate over all pairs of consecutive items in a given list
#Write a Python program to iterate over all pairs of consecutive items in a given list.
# Define a function 'pairwise' that iterates over all pairs of consecutive items in a list
def pairwise(l1):
    # Create an empty list 'temp' to store the pairs
    temp = []	
    
    # Iterate through the list elements up to the second-to-last element
    for i in range(len(l1) - 1):
        # Get the current element and the next element in the list
        current_element, next_element = l1[i], l1[i + 1]
        
        # Create a tuple 'x' containing the current and next elements
        x = (current_element, next_element)
        
        # Append the tuple 'x' to the 'temp' list
        temp.append(x)
    
    # Return the list of pairs
    return temp

# Create a list 'l1' with duplicate elements
l1 = [1, 1, 2, 3, 3, 4, 4, 5]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'l1'
print(l1)

# Iterate over all pairs of consecutive items in 'l1'
print("\nIterate over all pairs of consecutive items of the said list:")
# Call the 'pairwise' function with 'l1', then print the result
print(pairwise(l1))
