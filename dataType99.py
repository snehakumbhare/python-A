#Python: Find the maximum and minimum values in a given heterogeneous list
#Write a Python program to find the maximum and minimum values in a given heterogeneous list.
# Define a function 'max_min_val' that finds the maximum and minimum integer values in a list
def max_min_val(list_val):
    # Use generator expressions to find the maximum and minimum integer values in 'list_val'
    max_val = max(i for i in list_val if isinstance(i, int))
    min_val = min(i for i in list_val if isinstance(i, int))
    return (max_val, min_val)

# Create a list 'list_val' containing a mix of integers and non-integer values
list_val = ['Python', 3, 2, 4, 5, 'version']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list_val'
print(list_val)

# Print a message indicating the maximum and minimum integer values in the list will be determined
print("\nMaximum and Minimum values in the said list:")

# Call the 'max_min_val' function with 'list_val' and print the result
print(max_min_val(list_val)) 
