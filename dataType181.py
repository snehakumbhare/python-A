#Python: Iterate a given list cyclically on specific index position

#Write a  Python program to iterate a given list cyclically at a specific index position.
# Define a function called 'cyclically_iteration' that iterates a list cyclically based on a specific index position.
def cyclically_iteration(lst, spec_index):
    result = []  # Initialize an empty list to store the cyclically iterated elements.
    length = len(lst)  # Get the length of the input list.
    
    # Iterate through the list, starting from the 'spec_index' and wrapping around to the beginning if necessary.
    for i in range(length):
        element_index = spec_index % length  # Calculate the index of the current element based on 'spec_index'.
        result.append(lst[element_index])  # Append the element at the calculated index to the result list.
        spec_index += 1  # Increment 'spec_index' for the next iteration, to move to the next element.
    
    return result  # Return the list of cyclically iterated elements.

# Create a list of characters 'chars'.
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Print a message indicating the original list of characters.
print("Original list:")
print(chars)

# Specify a specific index position 'spec_index' for cyclic iteration and print a message.
spec_index = 3
print("\nIterate the said list cyclically on specific index position", spec_index, ":")
# Call the 'cyclically_iteration' function with 'chars' and 'spec_index' and print the result.
print(cyclically_iteration(chars, spec_index))

# Specify a different specific index position 'spec_index' for cyclic iteration and print a message.
spec_index = 5
print("\nIterate the said list cyclically on specific index position", spec_index, ":")
# Call the 'cyclically_iteration' function with 'chars' and the new 'spec_index' and print the result.
print(cyclically_iteration(chars, spec_index)) 
