#Python: Move a specified element in a given list

#Write a  Python program to move a specified element in a given list.

# Define a function 'group_similar_items' that moves a specified element to the end of a list.
def group_similar_items(seq, el):
    # Remove the specified element 'el' from the list and append it to the end.
    seq.append(seq.pop(seq.index(el)))
    return seq  # Return the modified list.

# Create a list 'colors' containing string elements.
colors = ['red', 'green', 'white', 'black', 'orange']

# Print a message indicating the original list of colors.
print("Original list:")
# Print the original 'colors' list.
print(colors)

# Specify the element 'el' to be moved to the end of the list.
el = "white"
# Print a message indicating the movement of 'el' to the end of the list.
print("Move", el, "at the end of the said list:")
# Call the 'group_similar_items' function with 'colors' and 'el', then print the result.
print(group_similar_items(colors, el))

# Revert to the original 'colors' list.
colors = ['red', 'green', 'white', 'black', 'orange']

# Print a message indicating the original list of colors.
print("\nOriginal list:")
# Print the original 'colors' list.
print(colors)

# Specify the element 'el' to be moved to the end of the list.
el = "red"
# Print a message indicating the movement of 'el' to the end of the list.
print("Move", el, "at the end of the said list:")
# Call the 'group_similar_items' function with 'colors' and 'el', then print the result.
print(group_similar_items(colors, el))

# Revert to the original 'colors' list.
colors = ['red', 'green', 'white', 'black', 'orange']

# Print a message indicating the original list of colors.
print("\nOriginal list:")
# Print the original 'colors' list.
print(colors)

# Specify the element 'el' to be moved to the end of the list.
el = "black"
# Print a message indicating the movement of 'el' to the end of the list.
print("Move", el, "at the end of the said list:")
# Call the 'group_similar_items' function with 'colors' and 'el', then print the result.
print(group_similar_items(colors, el))
