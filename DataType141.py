#Python: Remove empty lists from a given list of lists

#Write a  Python program to remove empty lists from a given list of lists.

# Create a list 'list1' that contains a mix of empty lists, strings, and sublists
list1 = [[], [], [], 'Red', 'Green', [1, 2], 'Blue', [], []]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the operation to remove empty lists
print("\nAfter deleting the empty lists from the said lists of lists")

# Create a new list 'list2' containing non-empty elements from 'list1'
list2 = [x for x in list1 if x]

# Print 'list2', which contains non-empty elements
print(list2)
