#Python: Remove consecutive duplicates of a given list

#Write a  Python program to remove consecutive (following each other continuously) 
# duplicates (elements) from a given list.
# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

# Define a function 'compress' that takes a list of numbers 'l_nums' as input
def compress(l_nums):
    # Use 'groupby' to group consecutive duplicates and return the unique keys
    return [key for key, group in groupby(l_nums)] 

# Define a list 'n_list' with consecutive duplicate elements
n_list = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]

# Print a message indicating the purpose of the following output
print("Original list:") 

# Print the original list 'n_list'
print(n_list)

# Print a message indicating the purpose of the following output
print("\nAfter removing consecutive duplicates:")

# Call the 'compress' function with 'n_list' as an argument and print the result with consecutive duplicates removed
print(compress(n_list))

