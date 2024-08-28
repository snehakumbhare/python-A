#Python: Zip two given lists of lists

#Write a  Python program to Zip two given lists of lists.

# Create two lists 'list1' and 'list2' containing sublists of numbers
list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]

# Print a message indicating the original lists
print("Original lists:")

# Print the contents of 'list1'
print(list1)

# Print the contents of 'list2'
print(list2)

# Use the 'map' function to add corresponding sublists from 'list1' and 'list2' together
result = list(map(list.__add__, list1, list2))

# Print a message indicating the zipped list
print("\nZipped list:\n" +  str(result))
