#Python: Create a list by concatenating a given list which range goes from 1 to n

#Write a  Python program to create a list by concatenating a given list with a range from 1 to n.

# Define a list 'my_list' containing elements 'p' and 'q'
my_list = ['p', 'q']

# Define a variable 'n' with the value 4
n = 4

# Use a list comprehension to create a new list 'new_list' by combining elements from 'my_list' with numbers from 1 to 'n'
new_list = ['{}{}'.format(x, y) for y in range(1, n+1) for x in my_list]

# Print the 'new_list' containing combinations of elements from 'my_list' and numbers
print(new_list)
