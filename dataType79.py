#Python: Remove the K'th element from a given list, print the new list

#Write a  Python program to remove the K'th element from a given list, and print the updated list
# Define a function 'remove_kth_element' that takes a list 'n_list' and an integer 'L' as input
def remove_kth_element(n_list, L):
    # Return a modified list by removing the element at the kth position (L-1) from the input list
    return n_list[:L - 1] + n_list[L:]

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'kth_position' with the value 3
kth_position = 3

# Call the 'remove_kth_element' function with 'n_list' and 'kth_position'
# and store the result in the 'result' variable
result = remove_kth_element(n_list, kth_position)

# Print a message indicating the list after removing an element at the kth position
print("\nAfter removing an element at the kth position of the said list:")
# Print the 'result' list
print(result) 
