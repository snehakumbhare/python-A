#Python Exercise: Sort a tuple by its float element

#Write a  Python program to sort a tuple by its float element.

# Create a list of tuples 'price', where each tuple represents an item and its price as a string.
price = [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Sort the 'price' list based on the price values (the second element in each tuple).
# The 'key' argument specifies a lambda function to convert the price strings to float values.
# Sorting is done in reverse (descending) order using the 'reverse' argument.
sorted_price = sorted(price, key=lambda x: float(x[1]), reverse=True)

# Print the 'sorted_price' list, which contains the items sorted by price in descending order.
print(sorted_price)
