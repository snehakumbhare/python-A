#Python: Find a tuple, the smallest second index value from a list of tuples

#Write a  Python program to find a tuple, the smallest second index value from a list of tuples.
# Define a list 'x' containing tuples, where each tuple has two elements
x = [(4, 1), (1, 2), (6, 0)]

# Use the 'min' function to find the minimum element in the list 'x' based on a custom key
# The 'key' argument specifies a lambda function that calculates a key for each element in 'x'
# The lambda function computes the key as a tuple, where the first element is the second element of the tuple (n[1]),
# and the second element is the negation of the first element (-n[0])
# This effectively sorts the tuples first by their second element in ascending order and then by their first element in descending order
# The 'min' function returns the tuple with the minimum key value
print(min(x, key=lambda n: (n[1], -n[0])))

