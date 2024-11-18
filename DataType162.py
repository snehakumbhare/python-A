#Python: Find the last occurrence of a specified item in a given list

#Write a  Python program to find the last occurrence of a specified item in a given list.
# Define a function called 'last_occurrence' that finds the last occurrence of a character 'ch' in a list of characters 'l1'.
def last_occurrence(l1, ch):
    # Join the list of characters into a single string and find the last index of the character 'ch'.
    return ''.join(l1).rindex(ch)

# Create a list 'chars' containing multiple characters.
chars = ['s', 'd', 'f', 's', 'd', 'f', 's', 'f', 'k', 'o', 'p', 'i', 'w', 'e', 'k', 'c']

# Print a message indicating the original list.
print("Original list:")
print(chars)

# Set the character 'ch' to 'f' and print a message indicating the last occurrence of 'ch' in the list, then call the 'last_occurrence' function.
ch = 'f'
print("Last occurrence of", ch, "in the said list:")
print(last_occurrence(chars, ch))

# Set the character 'ch' to 'c' and print a message indicating the last occurrence of 'ch' in the list, then call the 'last_occurrence' function.
ch = 'c'
print("Last occurrence of", ch, "in the said list:")
print(last_occurrence(chars, ch))

# Set the character 'ch' to 'k' and print a message indicating the last occurrence of 'ch' in the list, then call the 'last_occurrence' function.
ch = 'k'
print("Last occurrence of", ch, "in the said list:")
print(last_occurrence(chars, ch))

# Set the character 'ch' to 'w' and print a message indicating the last occurrence of 'ch' in the list, then call the 'last_occurrence' function.
ch = 'w'
print("Last occurrence of", ch, "in the said list:")
print(last_occurrence(chars, ch))
