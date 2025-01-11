#Python: Remove all the values except integer values from a given array of mixed values

#Write a  Python program to remove all values except integer values from a given array of mixed values.

# Define a function called 'test' that filters a list to include only integer values.
def test(lst):
    return [lst for lst in lst if isinstance(lst, int)]

# Create a list 'mixed_list' containing a mix of data types, including floats, integers, and strings.
mixed_list = [34.67, 12, -94.89, "Python", 0, "C#"]

# Print a message indicating the original list.
print("Original list:", mixed_list)

# Print a message indicating the purpose of the following lines of code.
print("After removing all the values except integer values from the said array of mixed values:")

# Call the 'test' function with 'mixed_list' and print the result, which contains only integer values.
print(test(mixed_list))
