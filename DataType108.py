#Python: Extract a specified column from a given nested list

#Write a  Python program to extract a specified column from a given nested list.

# Define a function 'remove_column' that extracts and removes a specified column from a nested list
def remove_column(nums, n):
   # Use a list comprehension to extract and remove the column 'n' from each sublist in 'nums'
   result = [i.pop(n) for i in nums]
   # Return the extracted values in the 'result' list
   return result 

# Create a nested list 'list1'
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# Set the column index 'n' to 0
n = 0

# Print a message indicating the original nested list
print("Original Nested list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the extraction of the 1st column
print("Extract 1st column:")

# Call the 'remove_column' function with 'list1' and 'n' and print the result
print(remove_column(list1, n))

# Create another nested list 'list2'
list2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Set the column index 'n' to 2
n = 2

# Print a message indicating the original nested list
print("\nOriginal Nested list:")
# Print the contents of 'list2'
print(list2)

# Print a message indicating the extraction of the 3rd column
print("Extract 3rd column:")

# Call the 'remove_column' function with 'list2' and 'n' and print the result
print(remove_column(list2, n))
