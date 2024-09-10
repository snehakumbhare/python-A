#Python: Sort a given matrix in ascending order according to the sum of its rows

#Write a  Python program to sort a given matrix in ascending order according to the sum of its rows.
# Define a function 'sort_matrix' that sorts a matrix in ascending order based on the sum of its rows
def sort_matrix(M):
    # Use the 'sorted' function to sort the matrix 'M' based on the sum of each row
    result = sorted(M, key=sum)
    return result

# Create two matrices 'matrix1' and 'matrix2'
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Print a message indicating the original matrix
print("Original Matrix:")
# Print the contents of 'matrix1'
print(matrix1)

# Print a message indicating the matrix will be sorted in ascending order based on row sums
print("\nSort the said matrix in ascending order according to the sum of its rows")

# Call the 'sort_matrix' function with 'matrix1' and print the result
print(sort_matrix(matrix1))

# Print a message indicating the original matrix
print("\nOriginal Matrix:")
# Print the contents of 'matrix2'
print(matrix2)

# Print a message indicating the matrix will be sorted in ascending order based on row sums
print("\nSort the said matrix in ascending order according to the sum of its rows")

# Call the 'sort_matrix' function with 'matrix2' and print the result
print(sort_matrix(matrix2))
