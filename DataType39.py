#Python: Convert a list of multiple integers into a single integer

#Write a  Python program to convert a list of multiple integers into a single integer.

# Define a list 'L' containing numeric elements
L = [11, 33, 50]

# Print the original list 'L'
print("Original List: ", L)

# Use the 'join' function to convert the elements of 'L' to a single string, then convert it to an integer 'x'
x = int("".join(map(str, L)))

# Print the single integer 'x'
print("Single Integer: ", x)
