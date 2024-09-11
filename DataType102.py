#Python: Extract specified size of strings from a give list of string values

#Write a  Python program to extract specified size of strings from a give list of string values.

# Define a function 'extract_string' that extracts strings of a specified length from a list
def extract_string(str_list1, l):
    # Use a list comprehension to filter strings in 'str_list1' with a length of 'l'
    result = [e for e in str_list1 if len(e) == l]
    return result

# Create a list 'str_list1' containing strings
str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'str_list1'
print(str_list1)

# Set the value of 'l' to 8
l = 8

# Print a message indicating the length of the string to extract
print("\nlength of the string to extract:")
# Print the value of 'l'
print(l)

# Print a message indicating that strings of the specified length will be extracted
print("\nAfter extracting strings of specified length from the said list:")

# Call the 'extract_string' function with 'str_list1' and 'l', then print the result
print(extract_string(str_list1, l)) 
