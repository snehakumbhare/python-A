#Python: Get unique values from a list

#Write a  Python program to get unique values from a list.

# Define a list 'my_list' containing multiple numbers, including duplicates
my_list = [10, 20, 30, 40, 20, 50, 60, 40]

# Print the original list 'my_list'
print("Original List : ", my_list)

# Convert the 'my_list' to a set 'my_set' to eliminate duplicates and keep unique elements
my_set = set(my_list)

# Convert the 'my_set' back to a list 'my_new_list' to obtain a list of unique numbers
my_new_list = list(my_set)

# Print the list of unique numbers stored in 'my_new_list'
print("List of unique numbers : ", my_new_list)
