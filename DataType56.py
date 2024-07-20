#Python: Convert a string to a list

#Write a  Python program to convert a string to a list.
# Import the 'ast' module, which provides a safe way to evaluate Python literals
import ast

# Define a string 'color' containing a Python list as a string
color = "['Red', 'Green', 'White']"

# Use the 'ast.literal_eval' function to safely evaluate the string as a Python literal expression
# This function ensures that the string is treated as a valid Python literal, in this case, a list
# Print the result, which is the actual list created from the string
print(ast.literal_eval(color)) 
