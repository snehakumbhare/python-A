#Python: Extend a list without append

#Write a Python program to extend a list without appending.

# Define two lists, 'x' and 'y', containing integers
x = [10, 20, 30]
y = [40, 50, 60]

# Use list slicing to insert the elements of 'y' at the beginning of 'x' by setting 'x[:0] = y'
x[:0] =y
# This effectively adds the elements of 'y' to the front of 'x'
print(x)
