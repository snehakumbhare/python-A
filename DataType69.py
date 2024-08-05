#Python: Remove duplicates from a list of lists

#Write a  Python program to remove duplicates from a list of lists.

# Import the 'itertools' module for working with iterators and grouping
import itertools

# Define a list 'num' containing sublists with integers
num = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]

# Print a message indicating the purpose of the following output
print("Original List", num)

# Sort the list 'num', which sorts the sublists lexicographically
num.sort()

# Use 'itertools.groupby' to group similar sublists and retain the first occurrence of each group
new_num = list(num for num, _ in itertools.groupby(num))

# Print a message indicating the purpose of the following output
print("New List", new_num)
