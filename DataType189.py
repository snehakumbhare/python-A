#Python: Shift last element to first position and first element to last position in a list

#Write a  Python program to shift last element to first position and first element to last position in a given list.

# Define a function called 'shift_first_last' that shifts the first element to the last position and the last element to the first position of a list.
def shift_first_last(lst):
    # Remove the first element and store it in 'x'.
    x = lst.pop(0)
    # Remove the last element and store it in 'y'.
    y = lst.pop()
    # Insert 'y' at the first position.
    lst.insert(0, y)
    # Insert 'x' at the last position.
    lst.insert(len(lst), x)
    return lst

# Create a list 'nums' containing integers.
nums = [1, 2, 3, 4, 5, 6, 7]

# Print a message indicating the original list.
print("Original list:")
# Print the original list 'nums'.
print(nums)

# Print a message indicating shifting the last element to the first position and the first element to the last position of the list.
print("Shift last element to first position and first element to last position of the said list:")
# Call the 'shift_first_last' function with 'nums' and print the result.
print(shift_first_last(nums))

# Create a list 'chars' containing characters.
chars = ['s', 'd', 'f', 'd', 's', 's', 'd', 'f']

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list 'chars'.
print(chars)

# Print a message indicating shifting the last element to the first position and the first element to the last position of the list.
print("Shift last element to first position and first element to last position of the said list:")
# Call the 'shift_first_last' function with 'chars' and print the result.
print(shift_first_last(chars)) 
