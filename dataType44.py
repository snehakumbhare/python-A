#Python: Generate groups of five consecutive numbers in a list
#Write a  Python program to generate groups of five consecutive numbers in a list.
# Create a nested list 'l' using a list comprehension
# This list comprehension generates a 5x5 matrix with elements calculated using the formula 5*i + j
l = [[5*i + j for j in range(1, 6)] for i in range(5)]

# Print the resulting 5x5 matrix 'l'
print(l)

