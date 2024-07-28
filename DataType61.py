#Python: Create a list of empty dictionaries

#Write a Python program to create a list of empty dictionaries.
# Define a variable 'n' and set it to the value 5
n = 5

# Create a list 'l' using a list comprehension, where each element is an empty dictionary
# The list comprehension creates 'n' empty dictionaries, and the list 'l' contains these dictionaries
l = [{} for _ in range(n)]

# Print the list 'l' containing 'n' empty dictionaries
print(l)
