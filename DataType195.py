#Python: Traverse a given list in reverse order, also print the elements with original index

#Write a  Python program to traverse a given list in reverse order, and print the elements with the original index.
# Create a list called 'color' containing string elements.
color = ["red", "green", "white", "black"]

# Print a message indicating the original list of colors.
print("Original list:")
# Print the original 'color' list.
print(color)

# Print a message indicating the traversal of the list in reverse order.
print("\nTraverse the said list in reverse order:")

# Use the 'reversed' function to iterate over the 'color' list in reverse order.
# 'i' represents each color element in reverse order.
for i in reversed(color):
    # Print each color element.
    print(i)

# Print a message indicating the traversal of the list in reverse order with the original index.
print("\nTraverse the said list in reverse order with original index:")

# Use 'reversed' in conjunction with 'enumerate' to iterate over the 'color' list in reverse order.
# 'i' is the original index, and 'el' represents each color element in reverse order.
for i, el in reversed(list(enumerate(color))):
    # Print the original index and the corresponding color element.
    print(i, el) 
