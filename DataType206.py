#Python: Common tuples between two given lists
#Write a Python program to find the common tuples between two given lists.
# Define a function 'test' that finds the common tuples between two lists of tuples.
def test(list1, list2):
    # Convert 'list1' and 'list2' into sets to remove duplicate tuples and make intersection easier.
    # Find the intersection (common tuples) between 'list1' and 'list2' using the 'intersection' method.
    result = set(list1).intersection(list2)
    # Convert the resulting set back to a list.
    return list(result)

# Define two lists of tuples 'list1' and 'list2'.
list1 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]
list2 = [('red', 'green'), ('orange', 'pink')]

# Print a message indicating the original lists.
print("\nOriginal lists:")
# Print the original lists 'list1' and 'list2'.
print(list1)
print(list2)

# Print a message indicating the purpose of the following lines of code.
print("\nCommon tuples between two said lists")
# Call the 'test' function to find the common tuples between 'list1' and 'list2' and print the result.
print(test(list1, list2))

# Define two different lists of tuples 'list1' and 'list2'.
list1 = [('red', 'green'), ('orange', 'pink')]
list2 = [('red', 'green'), ('black', 'white'), ('orange', 'pink')]

# Print a message indicating the original lists.
print("\nOriginal lists:")
# Print the original lists 'list1' and 'list2'.
print(list1)
print(list2)

# Print a message indicating the purpose of the following lines of code.
print("\nCommon tuples between two said lists")
# Call the 'test' function to find the common tuples between 'list1' and 'list2' and print the result.
print(test(list1, list2))
