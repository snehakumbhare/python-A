#Python: Remove words from a given list of strings containing a character or string
#Write a  Python program to remove words from a given list of strings containing a character or string.
# Define a function 'remove_words' that removes specific words from a list of strings
def remove_words(in_list, char_list):
    # Initialize an empty list to store the modified strings
    new_list = []
    
    # Iterate through each line in 'in_list'
    for line in in_list:
        # Split the line into words and join only those words that don't contain any phrase from 'char_list'
        new_words = ' '.join([word for word in line.split() if not any([phrase in word for phrase in char_list])])
        
        # Append the modified line to the 'new_list'
        new_list.append(new_words)
    
    return new_list

# Create a list of strings 'str_list'
str_list = ['Red color', 'Orange#', 'Green', 'Orange @', "White"]

# Print a message indicating the original list
print("Original list:")
print("list1:", str_list)

# Create a list of character phrases 'char_list'
char_list = ['#', 'color', '@']

# Print a message indicating the character list
print("\nCharacter list:")
print(char_list)

# Print a message indicating the new list after removing specific words
print("\nNew list:")
# Call the 'remove_words' function with 'str_list' and 'char_list', then print the result
print(remove_words(str_list, char_list)) 
