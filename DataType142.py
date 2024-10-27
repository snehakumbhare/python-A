#Python: Sum a specific column of a list in a given list of lists

#Write a  Python program to sum a specific column of a list in a given list of lists.

# Define a function 'sum_column' that calculates the sum of a specified column in a list of lists
def sum_column(nums, C):
    # Calculate the sum of the specified column 'C' using a generator expression
    result = sum(row[C] for row in nums)
    return result

# Create a list of lists 'nums' representing a 2D matrix
nums = [
        [1, 2, 3, 2],
        [4, 5, 6, 2],
        [7, 8, 9, 5],
    ]

# Print a message indicating the original list of lists
print("Original list of lists:")
# Print the contents of 'nums'
print(nums)

# Set the column index to 0
column = 0
# Print a message indicating the operation to sum the 1st column
print("\nSum: 1st column of the said list of lists:")
# Call the 'sum_column' function with 'nums' and column, then print the result
print(sum_column(nums, column))

# Set the column index to 1
column = 1
# Print a message indicating the operation to sum the 2nd column
print("\nSum: 2nd column of the said list of lists:")
# Call the 'sum_column' function with 'nums' and column, then print the result
print(sum_column(nums, column))

# Set the column index to 3
column = 3
# Print a message indicating the operation to sum the 4th column
print("\nSum: 4th column of the said list of lists:")
# Call the 'sum_column' function with 'nums' and column, then print the result
print(sum_column(nums, column)) 
