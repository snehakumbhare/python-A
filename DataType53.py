#Python: Create a list with infinite elements

#Write a  Python program to create a list with infinite elements.

# Import the 'itertools' module to work with iterators and generators
import itertools

# Create an iterator 'c' using the 'count' function from 'itertools'
# The 'count' function generates an infinite sequence of numbers starting from 0
c = itertools.count()

# Use the 'next' function to retrieve the next value from the iterator 'c' and print it
print(next(c))

# Retrieve and print the next value from the iterator 'c'
print(next(c))

# Retrieve and print the next value from the iterator 'c'
print(next(c))

# Retrieve and print the next value from the iterator 'c'
print(next(c))

# Retrieve and print the next value from the iterator 'c'
print(next(c)) 
