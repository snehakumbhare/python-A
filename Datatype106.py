#Python: Count integer in a given mixed list

#Write a  Python program to count integers in a given mixed list.
# Define a function 'count_integer' that counts the number of integers in a list
def count_integer(list1):
    # Initialize a counter 'ctr' to 0
    ctr = 0
    # Iterate through the elements of 'list1'
    for i in list1:
        # Check if the current element is an integer using 'isinstance'
        if isinstance(i, int):
            # Increment the counter if the element is an integer
            ctr = ctr + 1
    # Return the count of integers in the list
    return ctr

# Create a list 'list1' containing a mix of data types
list1 = [1, 'abcd', 3, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating that the number of integers in the list will be determined
print("\nNumber of integers in the said mixed list:")

# Call the 'count_integer' function with 'list1' and print the result
print(count_integer(list1))
