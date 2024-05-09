#Python Exercise: Converting a list of tuples into a dictionary

#Write a  Python program to convert a list of tuples into a dictionary.
# Create a list of tuples where each tuple contains two elements, a character and a number.
l = [("x", 1), ("x", 2), ("x", 3), ("y", 1), ("y", 2), ("z", 1)]

# Create an empty dictionary to store the results.
d = {}

# Iterate through each tuple (a, b) in the list 'l'.
for a, b in l:
    # Use 'setdefault' to create an empty list in the dictionary 'd' for the key 'a' if it doesn't exist.
    # Then, append the value 'b' to the list associated with key 'a'.
    d.setdefault(a, []).append(b)

# Print the resulting dictionary, where keys represent characters, and values are lists of corresponding numbers.
print(d) 
