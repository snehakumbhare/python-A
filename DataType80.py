#Python: Insert an element at a specified position into a given list

#Write a  Python program to insert an element at a specified position into a given list.
# Define a function 'insert_spec_position' that takes an element 'x', a list 'n_list', and an integer 'pos' as input
def insert_spec_position(x, n_list, pos):
    # Return a modified list by inserting the element 'x' at the specified position (pos-1) in the input list
    return n_list[:pos - 1] + [x] + n_list[pos - 1:]

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'kth_position' with the value 3
kth_position = 3

# Assign an integer 'x' with the value 12
x = 12

# Call the 'insert_spec_position' function with 'x', 'n_list', and 'kth_position'
# and store the result in the 'result' variable
result = insert_spec_position(x, n_list, kth_position)

# Print a message indicating the list after inserting an element at the kth position
print("\nAfter inserting an element at kth position in the said list:")
# Print the 'result' list
print(result)
