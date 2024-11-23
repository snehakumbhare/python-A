#Python: Convert a given list of strings into list of lists

#Write a  Python program to convert a given list of strings into a list of lists.
# Define a function called 'strings_to_listOflists' that converts a list of strings into a list of lists, where each character of a string is a separate element in a sublist.
def strings_to_listOflists(colors):
    # Use a list comprehension to create a new list 'result' where each string is converted into a list of its characters.
    result = [list(word) for word in colors]
    return result

# Create a list 'colors' containing string values.
colors = ["Red", "Maroon", "Yellow", "Olive"]

# Print a message indicating the original list of strings.
print('Original list of strings:')
print(colors)

# Print a message indicating the intention to convert the list of strings into a list of lists.
print("\nConvert the said list of strings into a list of lists:")

# Call the 'strings_to_listOflists' function to perform the conversion and print the result.
print(strings_to_listOflists(colors)) 
