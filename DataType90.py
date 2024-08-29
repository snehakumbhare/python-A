#Python: Count number of lists in a given list of lists

#Write a  Python program to count the number of lists in a given list of lists.

# Define a function 'count_list' that calculates the number of lists in the input list
def count_list(input_list):
    return len(input_list)

# Create two lists 'list1' and 'list2' containing sublists of varying depths
list1 = [[1, 3], [5, 7], [9, 11], [13, 15, 17]]
list2 = [[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]

# Print a message indicating the original list
print("Original list:")

# Print the contents of 'list1'
print(list1)

# Print a message indicating the number of lists in the first list of lists
print("\nNumber of lists in said list of lists:")

# Call the 'count_list' function with 'list1' and print the result
print(count_list(list1))

# Print a message indicating the original list
print("\nOriginal list:")

# Print the contents of 'list2'
print(list2)

# Print a message indicating the number of lists in the second list of lists
print("\nNumber of lists in said list of lists:")

# Call the 'count_list' function with 'list2' and print the result
print(count_list(list2)) 
