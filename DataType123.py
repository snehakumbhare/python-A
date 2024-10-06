#Python: Reverse strings in a given list of string values

#Write a  Python program to reverse strings in a given list of string values.
# Define a function 'reverse_strings_list' that reverses the strings in a list
def reverse_strings_list(string_list):
    # Use list comprehension to reverse each string in 'string_list'
    result = [x[::-1] for x in string_list]
    # Return the 'result' list with reversed strings
    return result

# Create a list 'colors_list' containing string values
colors_list = ["Red", "Green", "Blue", "White", "Black"]
# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'colors_list'
print(colors_list)
# Print a message indicating the operation to reverse the strings in the list
print("\nReverse strings of the said given list:")
# Call the 'reverse_strings_list' function with 'colors_list' and print the result
print(reverse_strings_list(colors_list))
