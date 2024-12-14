#Python: Convert a given list of tuples to a list of strings

#Write a  Python program to convert a given list of tuples to a list of strings.

# Define a function called 'tuples_to_list_str' that converts a list of tuples to a list of strings.
def tuples_to_list_str(lst):
    # Iterate through each tuple 'el' in the list 'lst'.
    # Convert each element in the tuple to a string using the '%s' format specifier, and join them with spaces.
    # Remove trailing spaces using 'strip'.
    result = [("%s " * len(el) % el).strip() for el in lst]
    return result

# Create a list of tuples 'colors', where each tuple contains color names.
colors = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]

# Print a message indicating the original list of tuples.
print("Original list of tuples:")
# Print the original list 'colors'.
print(colors)

# Call the 'tuples_to_list_str' function with 'colors' and store the result.
result_colors = tuples_to_list_str(colors)

# Print a message indicating the conversion of the list of tuples to a list of strings.
print("\nConvert the said list of tuples to a list of strings:")
# Print the result 'result_colors'.
print(result_colors)

# Create a list of tuples 'names', where each tuple contains names.
names = [('Laiba', 'Delacruz'), ('Mali', 'Stacey', 'Drummond'), ('Raja', 'Welch'), ('Saarah', 'Stone')]

# Print a message indicating the original list of tuples.
print("\nOriginal list of tuples:")
# Print the original list 'names'.
print(names)

# Call the 'tuples_to_list_str' function with 'names' and store the result.
result_names = tuples_to_list_str(names)

# Print a message indicating the conversion of the list of tuples to a list of strings.
print("\nConvert the said list of tuples to a list of strings:")
# Print the result 'result_names'.
print(result_names)
