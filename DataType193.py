#Python: Find the dimension of a given matrix

#Write a  Python program to find the dimension of a given matrix.
 # Define a function called 'matrix_dimensions' that calculates the number of rows and columns in a matrix (list of lists).
def matrix_dimensions(test_list):
    # Calculate the number of rows by finding the length of the input list.
    row = len(test_list)
    # Calculate the number of columns by finding the length of the first sub-list (assuming all sub-lists have the same length).
    column = len(test_list[0])
    return row, column  # Return the number of rows and columns as a tuple.

# Create a matrix 'lst' represented as a list of lists.
lst = [[1, 2], [2, 4]]

# Print a message indicating the original list (matrix).
print("\nOriginal list:")
# Print the original matrix 'lst'.
print(lst)

# Print a message indicating the dimensions of the matrix.
print("Dimension of the said matrix:")
# Call the 'matrix_dimensions' function with 'lst' and print the result (number of rows and columns).
print(matrix_dimensions(lst))

# Create another matrix 'lst' with a different number of rows and columns.
lst = [[0, 1, 2], [2, 4, 5]]

# Print a message indicating the original list (matrix).
print("\nOriginal list:")
# Print the original matrix 'lst'.
print(lst)

# Print a message indicating the dimensions of the matrix.
print("Dimension of the said matrix:")
# Call the 'matrix_dimensions' function with 'lst' and print the result (number of rows and columns).
print(matrix_dimensions(lst))

# Create another matrix 'lst' with a different number of rows and columns.
lst = [[0, 1, 2], [2, 4, 5], [2, 3, 4]]

# Print a message indicating the original list (matrix).
print("\nOriginal list:")
# Print the original matrix 'lst'.
print(lst)

# Print a message indicating the dimensions of the matrix.
print("Dimension of the said matrix:")
# Call the 'matrix_dimensions' function with 'lst' and print the result (number of rows and columns).
print(matrix_dimensions(lst)) 
