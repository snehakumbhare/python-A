#Python: Convert list to list of dictionaries

#Write a  Python program to convert a list to a list of dictionaries.
# Define a list 'color_name' containing color names
color_name = ["Black", "Red", "Maroon", "Yellow"]

# Define a list 'color_code' containing color codes
color_code = ["#000000", "#FF0000", "#800000", "#FFFF00"]

# Use a list comprehension to create a list of dictionaries by pairing elements from 'color_name' and 'color_code' using the 'zip' function
# Each dictionary has keys 'color_name' and 'color_code', and the values are taken from 'color_name' and 'color_code'
# This results in a list of dictionaries, where each dictionary represents a color with its name and code
# Print the list of color dictionaries
print([{'color_name': f, 'color_code': c} for f, c in zip(color_name, color_code)])
