#Python: Insert a specified element in a given list after every nth element
#Write a  Python program to insert a specified element in a given list after every nth element.
# Define a function called 'inset_element_list' that inserts an element 'x' into a list 'lst' after every 'n' elements.
def inset_element_list(lst, x, n):
    # Initialize a variable 'i' with the value of 'n'.
    i = n
    # Use a 'while' loop to iterate through the list 'lst'.
    while i < len(lst):
        # Insert the element 'x' at index 'i' in the list.
        lst.insert(i, x)
        # Increment 'i' by 'n+1' to skip 'n' elements and insert 'x' again after 'n' elements.
        i += n + 1
    # Return the modified list 'lst'.
    return lst

# Create a list of integers 'nums'.
nums = [1, 3, 5, 7, 9, 11, 0, 2, 4, 6, 8, 10, 8, 9, 0, 4, 3, 0]

# Print a message indicating the original list of integers.
print("Original list:")
print(nums)

# Define the element 'x' and the interval 'n' for inserting into the list.
x = 20
n = 4

# Print a message indicating the element to be inserted and the interval.
print("\nInsert", x, "in the said list after every", n, "th element:")

# Call the 'inset_element_list' function to insert 'x' into the list 'nums' after every 'n' elements and print the result.
print(inset_element_list(nums, x, n))

# Create a list of characters 'chars'.
chars = ['s', 'd', 'f', 'j', 's', 'a', 'j', 'd', 'f', 'd']

# Print a message indicating the original list of characters.
print("\nOriginal list:")
print(chars)

# Define the element 'x' and the interval 'n' for inserting into the list.
x = 'Z'
n = 3

# Print a message indicating the element to be inserted and the interval.
print("\nInsert", x, "in said list after every", n, "th element:")

# Call the 'inset_element_list' function to insert 'x' into the list 'chars' after every 'n' elements and print the result.
print(inset_element_list(chars, x, n)) 
