#Python: Remove a specified column from a given nested list

#Write a  Python program to remove a specified column from a given nested list.
# Define a function 'remove_column' that removes a specified column from a nested list
def remove_column(nums, n):
   # Iterate through the sublists in 'nums'
   for i in nums: 
      # Delete the element at index 'n' in each sublist
      del i[n] 
   # Return the modified 'nums' after removing the column
   return nums

# Create a nested list 'list1'
list1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]

# Set the column index 'n' to 0
n = 0

# Print a message indicating the original nested list
print("Original Nested list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating that the 1st column will be removed
print("After removing 1st column:")

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

# Print a message indicating that the 3rd column will be removed
print("After removing 3rd column:")

# Call the 'remove_column' function with 'list2' and 'n' and print the result
print(remove_column(list2, n)) 
