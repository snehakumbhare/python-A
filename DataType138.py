#Python: Sort a given mixed list of integers and strings

#Write a  Python program to sort a given mixed list of integers and strings. Numbers must be sorted before strings.
# Define a function 'sort_mixed_list' that sorts a mixed list of integers and strings
def sort_mixed_list(mixed_list):
    # Extract and sort the integer part of the list
    int_part = sorted([i for i in mixed_list if type(i) is int])
    # Extract and sort the string part of the list
    str_part = sorted([i for i in mixed_list if type(i) is str])
    # Combine the sorted integer and string parts and return the result
    return int_part + str_part

# Create a mixed list of integers and strings 'mixed_list'
mixed_list = [19, 'red', 12, 'green', 'blue', 10, 'white', 'green', 1]

# Print a message indicating the original mixed list
print("Original list:")
# Print the contents of 'mixed_list'
print(mixed_list)

# Sort the mixed list of integers and strings using the 'sort_mixed_list' function
print("\nSort the said mixed list of integers and strings:")
# Call the 'sort_mixed_list' function with 'mixed_list', then print the result
print(sort_mixed_list(mixed_list))
