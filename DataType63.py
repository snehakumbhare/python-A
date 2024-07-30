#Python: Insert a given string at the beginning of all items in a list

#Write a Python program to insert a given string at the beginning of all items in a list.
# Define a list 'num' containing integers
num = [1, 2, 3, 4]

# Use a list comprehension to create a new list of strings, where each string is formed by appending the index (formatted as a string) to the string 'emp'
# This effectively generates a list of strings with elements like 'emp1', 'emp2', 'emp3', 'emp4'
new_list = ['emp{0}'.format(i) for i in num]

# Print the new list 'new_list' containing the formatted strings
print(new_list)
