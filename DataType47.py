#Python: Insert an element before each element of a list

#Write a Python program to insert an element before each element of a list.
# Define a list 'color' containing color names
color = ['Red', 'Green', 'Black']

# Print the original list 'color'
print("Original List: ", color)

# Use a list comprehension to create a new list 'color' by inserting the letter 'c' before each element in the original list
# This results in each color name being duplicated with 'c' added in front of it
# Print the updated list 'color'
color = [v for elt in color for v in ('c', elt)]
print("Updated List: ", color)
