#Python: Split a list into different variables

#Write a  Python program to split a list into different variables.
# Define a list 'color' containing tuples, where each tuple represents a color with its name, hexadecimal code, and RGB value
color = [
    ("Black", "#000000", "rgb(0, 0, 0)"),
    ("Red", "#FF0000", "rgb(255, 0, 0)"),
    ("Yellow", "#FFFF00", "rgb(255, 255, 0)")
]

# Unpack the elements of the 'color' list into separate variables 'var1,' 'var2,' and 'var3'
var1, var2, var3 = color

# Print the first color tuple
print(var1)

# Print the second color tuple
print(var2)

# Print the third color tuple
print(var3)
