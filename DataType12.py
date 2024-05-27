#Python: Print a list after removing specified elements

#Write a  Python program to print a specified list after removing the 0th, 4th and 5th elements.

# Create a list 'color' with several color strings
color = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

# Use a list comprehension to create a new list 'color' that includes elements from the original list
# but only if their index (i) is not in the specified indices (0, 4, 5)
color = [x for (i, x) in enumerate(color) if i not in (0, 4, 5)]

# Print the modified 'color' list, which excludes elements at indices 0, 4, and 5
print(color)
