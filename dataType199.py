#Python: Convert a given unicode list to a list contains strings

#Write a  Python program to convert a Unicode list to a list of strings.
# Define a function 'unicode_to_str' that converts a list of unicode strings to a list of regular strings.
def unicode_to_str(lst):
    # Use a list comprehension to iterate over each element 'x' in 'lst' and convert it to a regular string using 'str()'.
    result = [str(x) for x in lst]
    return result

# Create a list of unicode strings 'students'.
students = [u'S001', u'S002', u'S003', u'S004']

# Print a message indicating the original list.
print("Original lists:")
# Print the original list of unicode strings.
print(students)

# Print a message indicating the purpose of the following line of code.
print("Convert the said unicode list to a list containing strings:")
# Call the 'unicode_to_str' function to convert the list of unicode strings to a list of regular strings.
print(unicode_to_str(students))
