#Python: Find the list in a list of lists whose sum of elements is the highest

#Write a Python program to find the list in a list of lists whose sum of elements is the highest.

# Define a list 'num' containing sublists, each with three integers
num = [[1, 2, 3], [4, 5, 6], [10, 11, 12], [7, 8, 9]]

# Use the 'max' function to find the maximum sublist in 'num' based on the sum of its elements
# The 'key' argument specifies a lambda function that calculates the sum of each sublist
# The 'max' function returns the sublist with the maximum sum
print(max(num, key=sum)) 
