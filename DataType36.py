#Python: Get variable unique identification number or string

#Write a  Python program to get a variable with an identification number or string.

# Define a variable 'x' and set its value to 100
x = 100

# Print the hexadecimal representation of the unique identifier (memory address) of 'x'
# 'id(x)' returns the memory address, and 'format(id(x), 'x')' formats it as a hexadecimal string
print(format(id(x), 'x'))

# Define a string 's' with the value 'w3resource'
s = 'w3resource'

# Print the hexadecimal representation of the unique identifier (memory address) of the string 's'
# 'id(s)' returns the memory address, and 'format(id(s), 'x')' formats it as a hexadecimal string
print(format(id(s), 'x'))
