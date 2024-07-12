#Python: Sort a list of nested dictionaries
#Write a  Python program to sort a list of nested dictionaries.
# Define a list 'my_list' containing dictionaries, where each dictionary has a 'key' that contains another dictionary with a 'subkey'
my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]

# Print the original list 'my_list'
print("Original List: ")
print(my_list)

# Sort the list 'my_list' based on the value of 'subkey' within each dictionary
# The 'key' argument of the 'sort' method is a lambda function that extracts the 'subkey' value for sorting
# Sorting is performed in descending order by using the 'reverse=True' parameter
# Print the sorted list
my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
print("Sorted List: ")
print(my_list) 
