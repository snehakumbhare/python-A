#Python: Find the items start with specific character from a given list

#Write a  Python program to find items starting with a specific character from a list.
# Define a function 'test' that takes a list 'lst' and a character 'char' as arguments
def test(lst, char):
    # Use a list comprehension to filter elements in 'lst' that start with the specified 'char'
    result = [i for i in lst if i.startswith(char)]
    return result
# Define a list 'text' containing strings
text = ["abcd", "abc", "bcd", "bkie", "cder", "cdsw", "sdfsd", "dagfa", "acjd"]
# Print a message indicating the purpose of the following output
print("\nOriginal list:")
print(text)
# Define a character 'char'
char = "a"
# Print a message indicating the purpose of the following output
print("\nItems start with", char, "from the said list:")
# Call the 'test' function with 'text' and 'char' as arguments and print the result
print(test(text, char))
# Change the value of 'char' to "d"
char = "d"
# Print a message indicating the purpose of the following output
print("\nItems start with", char, "from the said list:")
# Call the 'test' function with 'text' and the updated 'char' as arguments and print the result
print(test(text, char))
# Change the value of 'char' to "w"
char = "w"
# Print a message indicating the purpose of the following output
print("\nItems start with", char, "from the said list:")
# Call the 'test' function with 'text' and the updated 'char' as arguments and print the result
print(test(text, char))
