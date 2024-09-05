#Python: Sort a list of lists by length and value

#Write a  Python program to sort a given list of lists by length and value.

# Define a function 'sort_sublists' that sorts a list of lists by length and values
def sort_sublists(input_list):
    input_list.sort()  # Sort the list by sublist contents
    input_list.sort(key=len)  # Sort the list by the length of sublists
    return input_list

# Create a list 'list1' containing sublists of numbers
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'list1'
print(list1)

# Print a message indicating the sorted list of lists by length and values
print("\nSort the list of lists by length and value:")
# Call the 'sort_sublists' function with 'list1' and print the result
print(sort_sublists(list1))
