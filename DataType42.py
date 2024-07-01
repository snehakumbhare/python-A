#Python: Find missing and additional values in two lists

#Write a  Python program to find missing and additional values in two lists.
# Define two lists 'list1' and 'list2' containing elements
list1 = ['a', 'b', 'c', 'd', 'e', 'f']
list2 = ['d', 'e', 'f', 'g', 'h']

# Calculate the missing values in 'list2' by finding the set difference between 'list1' and 'list2'
missing_values = set(list1).difference(list2)

# Print the missing values in the second list 'list2'
print('Missing values in the second list: ', ','.join(missing_values))

# Calculate the additional values in 'list2' by finding the set difference between 'list2' and 'list1'
additional_values = set(list2).difference(list1)

# Print the additional values in the second list 'list2'
print('Additional values in the second list: ', ','.join(additional_values))
