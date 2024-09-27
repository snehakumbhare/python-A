#Python: Remove all elements from a given list present in another list
#Write a  Python program to remove all elements from a given list that are present in another list.
# Define a function 'index_on_inner_list' that removes elements from list1 that are also in list2
def index_on_inner_list(list1, list2):
    # Use a list comprehension to iterate through list1 and keep elements that are not in list2
    result = [x for x in list1 if x not in list2]
    return result

# Create two lists 'list1' and 'list2'
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [2, 4, 6, 8]

# Print messages indicating the original lists
print("Original lists:")
print("list1:", list1)
print("list2:", list2)

# Print a message indicating the operation to remove elements from 'list1' present in 'list2'
print("\nRemove all elements from 'list1' that are also present in 'list2:")
# Call the 'index_on_inner_list' function with 'list1' and 'list2' and print the result
print(index_on_inner_list(list1, list2)) 
