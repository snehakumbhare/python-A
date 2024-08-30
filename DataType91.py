#Python: Find the list with maximum and minimum length

#Write a  Python program to find a list with maximum and minimum lengths.
# Define a function 'max_length_list' that finds the maximum length and the list with the maximum length in 'input_list'
def max_length_list(input_list):
    # Find the maximum length of lists in 'input_list'
    max_length = max(len(x) for x in input_list)
    # Find the list with the maximum length in 'input_list'
    max_list = max(input_list, key=len)
    return (max_length, max_list)

# Define a function 'min_length_list' that finds the minimum length and the list with the minimum length in 'input_list'
def min_length_list(input_list):
    # Find the minimum length of lists in 'input_list'
    min_length = min(len(x) for x in input_list)
    # Find the list with the minimum length in 'input_list'
    min_list = min(input_list, key=len)
    return (min_length, min_list)

# Create a list 'list1' containing sublists of varying lengths
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]

# Print a message indicating the original list
print("Original list:")

# Print the contents of 'list1'
print(list1)

# Print a message indicating the list with the maximum length of sublists
print("\nList with maximum length of lists:")

# Call the 'max_length_list' function with 'list1' and print the result
print(max_length_list(list1))

# Print a message indicating the list with the minimum length of sublists
print("\nList with minimum length of lists:")

# Call the 'min_length_list' function with 'list1' and print the result
print(min_length_list(list1))

# Create a different list 'list1' containing sublists of varying lengths
list1 = [[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]

# Print a message indicating the original list
print("Original list:")

# Print the contents of the new 'list1'
print(list1)

# Print a message indicating the list with the maximum length of sublists
print("\nList with maximum length of lists:")

# Call the 'max_length_list' function with the new 'list1' and print the result
print(max_length_list(list1))

# Print a message indicating the list with the minimum length of sublists
print("\nList with minimum length of lists:")

# Call the 'min_length_list' function with the new 'list1' and print the result
print(min_length_list(list1))

# Create another list 'list1' containing sublists of varying lengths
list1 = [[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]

# Print a message indicating the original list
print("Original list:")

# Print the contents of the new 'list1'
print(list1)

# Print a message indicating the list with the maximum length of sublists
print("\nList with maximum length of lists:")

# Call the 'max_length_list' function with the new 'list1' and print the result
print(max_length_list(list1))

# Print a message indicating the list with the minimum length of sublists
print("\nList with minimum length of lists:")

# Call the 'min_length_list' function with the new 'list1' and print the result
print(min_length_list(list1))
