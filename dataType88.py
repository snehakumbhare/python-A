#Python: Read a square matrix from console and print the sum of matrix primary diagonal
#Write a  Python program to read a square matrix from the console and print the sum of the matrix's primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user.
# Prompt the user to input the size of the square matrix
size = int(input("Input the size of the matrix: "))

# Create a square matrix filled with zeros using list comprehensions based on the size
matrix = [[0] * size for row in range(0, size)]

# Iterate through each row and column to populate the matrix with input values
for x in range(0, size):
    # Read a line of space-separated integers and convert them to a list of integers
    line = list(map(int, input().split()))
    
    for y in range(0, size):
        # Populate the matrix with the input elements
        matrix[x][y] = line[y]

# Calculate the sum of the primary diagonal elements of the matrix
matrix_sum_diagonal = sum(matrix[size - i - 1][size - i - 1] for i in range(size))

# Print a message indicating the sum of the primary diagonal of the matrix
print("Sum of matrix primary diagonal:")
# Print the sum of the primary diagonal
print(matrix_sum_diagonal) 
