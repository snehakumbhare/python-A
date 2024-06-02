#Python: Generate all permutations of a list in Python

#Write a  Python program to generate all permutations of a list in  Python.

# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Use 'itertools.permutations' to generate all permutations of the list [1, 2, 3], and convert the result to a list
# This will produce all possible orderings of the elements in the list
print(list(itertools.permutations([1, 2, 3])))
