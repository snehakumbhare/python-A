#Python: Create a list reflecting the run-length encoding from a list
#Write a  Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters.
# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

# Define a function 'encode_list' that takes a list 's_list' as input
def encode_list(s_list):
    # Use 'groupby' to group consecutive elements and count their occurrences
    return [[len(list(group)), key] for key, group in groupby(s_list)]

# Define a list 'n_list' with various elements including duplicates
n_list = [1, 1, 2, 3, 4, 4.3, 5, 1]

# Print a message indicating the purpose of the following output
print("Original list:") 

# Print the original list 'n_list'
print(n_list)

# Print a message indicating the purpose of the following output
print("\nList reflecting the run-length encoding from the said list:")

# Call the 'encode_list' function with 'n_list' as an argument and print the result of run-length encoding
print(encode_list(n_list))

# Reassign 'n_list' with a string
n_list = 'automatically'

# Print a message indicating the purpose of the following output
print("\nOriginal String:") 

# Print the original string 'n_list'
print(n_list)

# Print a message indicating the purpose of the following output
print("\nList reflecting the run-length encoding from the said string:")

# Call the 'encode_list' function with 'n_list' as an argument and print the result of run-length encoding for the string
print(encode_list(n_list)) 
