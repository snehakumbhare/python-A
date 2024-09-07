#Python: Scramble the letters of string in a given list

#Write a  Python program to scramble the letters of a string in a given list.
# Import the 'shuffle' function from the 'random' module
from random import shuffle

# Define a function 'shuffle_word' that shuffles the characters in a word
def shuffle_word(text_list):
    # Convert the input word to a list of characters
    text_list = list(text_list)
    # Shuffle the characters in the list
    shuffle(text_list)
    # Convert the shuffled list back to a string and return it
    return ''.join(text_list)

# Create a list 'text_list' containing strings
text_list = ['Python', 'list', 'exercises', 'practice', 'solution']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'text_list'
print(text_list)

# Print a message indicating the letters in the strings will be scrambled
print("\nAfter scrambling the letters of the strings of the said list:")

# Use a list comprehension to apply the 'shuffle_word' function to each word in 'text_list' and print the result
result = [shuffle_word(word) for word in text_list]
print(result)
