#Python: Remove duplicate dictionary from a given list

#Write a  Python program to remove duplicate dictionary entries from a given list.
# Define a function 'remove_duplicate_dictionary' that removes duplicate dictionaries from a list
def remove_duplicate_dictionary(list_color):
    # Use a set comprehension to convert each dictionary in the list to a tuple and remove duplicates
    # Then, convert the unique tuples back to dictionaries
    result = [dict(e) for e in {tuple(d.items()) for d in list_color}]
    return result

# Create a list 'list_color' containing dictionaries with color names as keys and hexadecimal color codes as values
list_color = [{'Green': '#008000'}, {'Black': '#000000'}, {'Blue': '#0000FF'}, {'Green': '#008000'}]

# Print a message indicating the original list with duplicate dictionaries
print ("Original list with duplicate dictionary:")
# Print the contents of the 'list_color' list
print(list_color)

# Print a message indicating the operation to remove duplicate dictionaries
print("\nAfter removing duplicate dictionary of the said list:")

# Call the 'remove_duplicate_dictionary' function with 'list_color' and print the result
print(remove_duplicate_dictionary(list_color))
