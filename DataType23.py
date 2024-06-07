#Python: Flatten a shallow list

#Write a  Python program to flatten a shallow list.
# Import the 'itertools' module, which provides various functions for working with iterators
import itertools

# Define a list 'original_list' containing nested sublists
original_list = [[2, 4, 3], [1, 5, 6], [9], [7, 9, 0]]

# Use 'itertools.chain' and the unpacking operator (*) to merge the sublists into a single flat list
new_merged_list = list(itertools.chain(*original_list))

# Print the newly merged list 'new_merged_list'
print(new_merged_list)
