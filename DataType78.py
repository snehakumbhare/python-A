#Python: Split a given list into two parts where the length of the first part of the list is given
#Write a  Python program to split a given list into two parts where the length of the first part of the list is given.
# Define a function 'split_two_parts' that takes a list 'n_list' and an integer 'L' as input
def split_two_parts(n_list, L):
    # Return two parts of the input list: the first 'L' elements and the rest of the list
    return n_list[:L], n_list[L:]

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'first_list_length' with the value 3
first_list_length = 3

# Print a message indicating the length of the first part of the list
print("\nLength of the first part of the list:", first_list_length)

# Print a message indicating that the list is being split into two parts
print("\nSplit the said list into two parts:")
# Call the 'split_two_parts' function with 'n_list' and 'first_list_length', and print the result
print(split_two_parts(n_list, first_list_length)) 
