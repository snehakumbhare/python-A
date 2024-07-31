#Python: Iterate over two lists simultaneously

#Write a Python program to iterate over two lists simultaneously.
# Define two lists 'num' and 'color' containing integers and color names, respectively
num = [1, 2, 3]
color = ['red', 'white', 'black']

# Use a 'for' loop and the 'zip' function to iterate over pairs of elements from 'num' and 'color' in parallel
# In each iteration, the variables 'a' and 'b' will hold the values from 'num' and 'color', respectively
# Print the values of 'a' and 'b' in each iteration
for (a, b) in zip(num, color):
    print(a, b)

