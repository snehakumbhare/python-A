#Python: Convert a pair of values into a sorted unique array

#Write a  Python program to convert a pair of values into a sorted unique array.

# Define a list 'L' containing tuples with pairs of numbers
L = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4), (7, 8), (9, 10)]

# Print the original list 'L'
print("Original List: ", L)

# Use a set to remove duplicate pairs of numbers and the 'union' method to merge all unique pairs
# Sort the resulting set and print the sorted unique data
print("Sorted Unique Data:", sorted(set().union(*L)))
