#Python: Check whether all items of a list is equal to a given string

#Write a Python program to check if all items in a given list of strings are equal to a given string.

# Define a list 'color1' containing color names
color1 = ["green", "orange", "black", "white"]

# Define another list 'color2' containing color names, with multiple occurrences of 'green'
color2 = ["green", "green", "green", "green"]

# Check if all elements in 'color1' are equal to 'blue' using a generator expression and the 'all' function
# The 'all' function returns True if all elements in the iterable are True (in this case, if all elements are 'blue')
# Since there is no 'blue' in 'color1', this will return False
print(all(c == 'blue' for c in color1))

# Check if all elements in 'color2' are equal to 'green' using a generator expression and the 'all' function
# The 'all' function returns True if all elements in the iterable are True (in this case, if all elements are 'green')
# Since all elements in 'color2' are 'green', this will return True
print(all(c == 'green' for c in color2)) 
