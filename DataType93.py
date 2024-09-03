#Python: Count the number of sublists contain a particular element

#Write a  Python program to count the number of sublists that contain a particular element.
# Define a function 'count_element_in_list' that counts the occurrences of element 'x' in 'input_list'
def count_element_in_list(input_list, x):
    ctr = 0
    for i in range(len(input_list)):
        if x in input_list[i]:
            ctr += 1
    return ctr

# Create a list 'list1' containing sublists of elements
list1 = [[1, 3], [5, 7], [1, 11], [1, 15, 7]]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the count of the element '1' in the list
print("\nCount 1 in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the element '1', then print the result
print(count_element_in_list(list1, 1))

# Print a message indicating the count of the element '7' in the list
print("\nCount 7 in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the element '7', then print the result
print(count_element_in_list(list1, 7))

# Create a list 'list1' containing sublists of characters
list1 = [['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the count of the character 'A' in the list
print("\nCount 'A' in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the character 'A', then print the result
print(count_element_in_list(list1, 'A'))

# Print a message indicating the count of the character 'E' in the list
print("\nCount 'E' in the said list:")
# Call the 'count_element_in_list' function with 'list1' and the character 'E', then print the result
print(count_element_in_list(list1, 'E'))

