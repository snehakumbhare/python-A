#Python: Remove specific words from a given list

#Write a  Python program to remove specific words from a given list.
# Define a function 'remove_words' that removes specified words from a list
def remove_words(list1, remove_words):
    # Iterate through the elements in 'list1'
    for word in list(list1):
        # Check if the word is in the 'remove_words' list
        if word in remove_words:
            # If it is, remove the word from 'list1'
            list1.remove(word)
    return list1

# Create a list 'colors' and a list of words to remove 'remove_colors'
colors = ['red', 'green', 'blue', 'white', 'black', 'orange']
remove_colors = ['white', 'orange']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'colors'
print(colors)

# Print a message indicating the words to remove
print("\nRemove words:")
# Print the contents of 'remove_colors'
print(remove_colors)

# Print a message indicating the operation to remove specified words
print("\nAfter removing the specified words from the said list:")
# Call the 'remove_words' function with 'colors' and 'remove_colors', then print the result
print(remove_words(colors, remove_colors))
