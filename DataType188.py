#Python: Sort a given list of tuples on specified element

#Write a  Python program to sort a given list of tuples by a specified element.
# Define a function called 'sort_on_specific_item' that sorts a list of tuples based on a specific element of each tuple.
def sort_on_specific_item(lst, n):
    # Sort the list 'lst' based on the element at index 'n' of each tuple.
    result = sorted(lst, key=lambda x: x[n])
    return result
	
# Create a list of tuples 'items', where each tuple contains items with three elements.
items = [('item2', 10, 10.12), ('item3', 15, 25.10), ('item1', 11, 24.50), ('item4', 12, 22.50)]

# Print a message indicating the original list of tuples.
print("Original list of tuples:")
# Print the original list 'items'.
print(items)

# Print a message indicating sorting based on the 1st element (index 0) of the tuple in the list.
print("\nSort on 1st element of the tuple of the said list:")
# Call the 'sort_on_specific_item' function with 'items' and index '0' for the 1st element.
n = 0
# Print the result of the sorting.
print(sort_on_specific_item(items, n))

# Print a message indicating sorting based on the 2nd element (index 1) of the tuple in the list.
print("\nSort on 2nd element of the tuple of the said list:")
# Call the 'sort_on_specific_item' function with 'items' and index '1' for the 2nd element.
n = 1
# Print the result of the sorting.
print(sort_on_specific_item(items, n))

# Print a message indicating sorting based on the 3rd element (index 2) of the tuple in the list.
print("\nSort on 3rd element of the tuple of the said list:")
# Call the 'sort_on_specific_item' function with 'items' and index '2' for the 3rd element.
n = 2
# Print the result of the sorting.
print(sort_on_specific_item(items, n)) 
