#Python: Select an item randomly from a list
#Write a  Python program to select an item randomly from a list.

#Use random.choice() to get a random element from a given list.
# Import the 'random' module, which provides functions for generating random values
import random
# Define a list 'color_list' containing various colors
color_list = ['Red', 'Blue', 'Green', 'White', 'Black']

# Use the 'random.choice' function to select and print a random color from the 'color_list'
print(random.choice(color_list))

#Sample Solution-2:
# Import the 'choice' function from the 'random' module to select a random element from a list

#from random import choice

# Define a function named 'random_element' that takes a list 'lst' as a parameter
#def random_element(lst):
    # Use the 'choice' function to return a random element from the input list 'lst'
   # return choice(lst)

# Call the 'random_element' function with a list as an argument and print the randomly selected element
#print(random_element([2, 3, 4, 7, 9, 11, 15]))
