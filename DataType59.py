#Python: Check whether the n-th element exists in a given list

#Write a Python program to check whether the n-th element exists in a given list.

# Define a list 'x' containing integers
x = [1, 2, 3, 4, 5, 6]

# Calculate the length of the list 'x' using the 'len' function and subtract 1 to get the last element's index
xlen = len(x) - 1

# Print the last element of the list 'x' using its index, which is 'xlen'
print(x[xlen])
