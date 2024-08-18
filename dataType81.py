#Python: Extract a given number of randomly selected elements from a given list
#Write a  Python program to extract a given number of randomly selected elements from a given list.
# Import the 'random' module to generate random numbers
import random

# Define a function 'random_select_nums' that takes a list 'n_list' and an integer 'n' as input
def random_select_nums(n_list, n):
    # Use 'random.sample' to select 'n' random elements from the input list 'n_list'
    return random.sample(n_list, n)

# Create a list 'n_list' containing integers
n_list = [1, 1, 2, 3, 4, 4, 5, 1]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'selec_nums' with the value 3
selec_nums = 3

# Call the 'random_select_nums' function with 'n_list' and 'selec_nums'
# and store the result in the 'result' variable
result = random_select_nums(n_list, selec_nums)

# Print a message indicating the selection of 3 random numbers from the above list
print("\nSelected 3 random numbers of the above list:")
# Print the 'result' list containing the randomly selected numbers
print(result)
