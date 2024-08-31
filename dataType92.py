#Python: Check if a nested list is a subset of another nested list
#Write a  Python program to check if a nested list is a subset of another nested list.
# Define a function 'checkSubset' that checks if all elements of 'input_list2' are contained in 'input_list1'
def checkSubset(input_list1, input_list2):
    return all(map(input_list1.__contains__, input_list2))

# Create two lists 'list1' and 'list2'
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[1, 3], [13, 15, 17]]

# Print a message indicating the original lists
print("Original list:")
# Print the contents of 'list1'
print(list1)
# Print the contents of 'list2'
print(list2)

# Check if one of the lists is a subset of the other and print the result
print("\nIf one of the said list is a subset of another:")
print(checkSubset(list1, list2))

# Create two nested lists 'list1' and 'list2'
list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
list2 = [[[3, 4], [5, 6]]]

# Print a message indicating the original lists
print("Original list:")
# Print the contents of 'list1'
print(list1)
# Print the contents of 'list2'
print(list2)

# Check if one of the lists is a subset of the other and print the result
print("\nIf one of the said list is a subset of another:")
print(checkSubset(list1, list2))

# Create two nested lists 'list1' and 'list2' with different elements
list1 = [[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
list2 = [[[3, 4], [5, 6]]]

# Print a message indicating the original lists
print("Original list:")
# Print the contents of 'list1'
print(list1)
# Print the contents of 'list2'
print(list2)

# Check if one of the lists is a subset of the other and print the result
print("\nIf one of the said list is a subset of another:")
print(checkSubset(list1, list2)) 
