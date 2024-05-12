#Python Exercise: Replace last value of tuples in a list

#Write a  Python program to replace the last value of tuples in a list.

# Create a list of tuples, where each tuple contains three numbers.
l = [(10, 20, 40), (40, 50, 60), (70, 80, 90)]

# Use a list comprehension to iterate through each tuple 't' in the list 'l'.
# For each tuple, create a new tuple by removing the last element and adding the number 100.
# The result is a list of modified tuples.
print([t[:-1] + (100,) for t in l]) 
