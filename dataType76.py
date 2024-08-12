#Python: Create a list reflecting the modified run-length encoding

#Write a  Python program to create a list reflecting the modified run-length
#encoding from a given list of integers or a given list of characters.

# Import the 'groupby' function from the 'itertools' module
from itertools import groupby

# Define a function 'modified_encode' that takes a list 'alist' as input
def modified_encode(alist):
    # Define a nested function 'ctr_ele' to process elements within the list
    def ctr_ele(el):
        # Check if the length of the element is greater than 1
        if len(el) > 1:
            # If yes, return a list with the count and the first element
            return [len(el), el[0]]
        else:
            # If not, return the first element
            return el[0]
    
    # Apply the 'ctr_ele' function to groups of identical elements using 'groupby'
    # and store the results in a list comprehension
    return [ctr_ele(list(group)) for key, group in groupby(alist)]

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Print a message indicating the modified run-length encoded list
print("\nList reflecting the modified run-length encoding from the said list:")
# Call the 'modified_encode' function with 'n_list' and print the result
print(modified_encode(n_list))

# Create a string 'n_list' containing characters
n_list = 'aabcddddadnss'

# Print a message indicating the original string
print("\nOriginal String:")
# Print the original string
print(n_list)

# Print a message indicating the modified run-length encoded list
print("\nList reflecting the modified run-length encoding from the said string:")
# Call the 'modified_encode' function with 'n_list' and print the result
print(modified_encode(n_list)) 
