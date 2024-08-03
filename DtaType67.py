#Python: Find all the values in a list are greater than a specified number
#Write a  Python program to find all the values in a list that are greater than a specified number.
# Define two lists, 'list1' and 'list2', containing integers
list1 = [220, 330, 500]
list2 = [12, 17, 21]

# Check if all elements in 'list1' are greater than or equal to 200 using a generator expression and the 'all' function
# The 'all' function returns 'True' if all elements meet the condition, otherwise 'False'
print(all(x >= 200 for x in list1))

# Check if all elements in 'list2' are greater than or equal to 25 using a generator expression and the 'all' function
# The 'all' function returns 'True' if all elements meet the condition, otherwise 'False'
print(all(x >= 25 for x in list2))
