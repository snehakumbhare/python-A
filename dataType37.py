#Python: Find common items from two lists
#Write a  Python program to find common items in two lists.
# Define a tuple 'color1' containing color names
color1 = "Red", "Green", "Orange", "White"

# Define another tuple 'color2' containing color names
color2 = "Black", "Green", "White", "Pink"

# Create sets from 'color1' and 'color2' to perform set intersection (common elements)
# Print the result, which contains the colors that are common to both sets
print(set(color1) & set(color2))
