#Python: Read a matrix from console and print the sum for each column

#Write a  Python program to read a matrix from the console and print the sum for each column. 
#As input from the user, accept matrix rows, columns, and elements separated by a space (each row).
# Prompt the user to input the number of rows for the matrix
rows = int(input("Input rows: "))

# Prompt the user to input the number of columns for the matrix
columns = int(input("Input columns: "))

# Create a 2D matrix filled with zeros using list comprehensions based on the number of rows and columns
matrix = [[0]*columns for row in range(rows)]

# Prompt the user to input the elements for each row in the matrix
print('Input number of elements in a row (1, 2, 3): ')
for row in range(rows):
    # Read a line of space-separated integers and convert them to a list of integers
    lines = list(map(int, input().split()))
    for column in range(columns):
        # Populate the matrix with the input elements
        matrix[row][column] = lines[column]

# Create a list 'sum' initialized with zeros to store the sum for each column
sum = [0]*columns

# Print a message indicating the calculation of the sum for each column
print("Sum for each column:")

# Iterate over each column
for column in range(columns):
    # Calculate the sum of the elements in the current column by iterating through the rows
    for row in range(rows):
        sum[column] += matrix[row][column]
    
    # Print the sum for the current column followed by a space
    print((sum[column]), ' ', end = '')
