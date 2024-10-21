#Python: Remove duplicate words from a given list of strings

#Write a Python program to remove duplicate words from a given list of strings.

# Define a function 'unique_list' that removes duplicates from a list
def unique_list(l):
    # Create an empty list 'temp' to store unique elements
    temp = []
    
    # Iterate through the elements of the input list 'l'
    for x in l:
        # Check if the element 'x' is not in the 'temp' list (i.e., it's unique)
        if x not in temp:
            # Append the unique element 'x' to the 'temp' list
            temp.append(x)
    
    # Return the list of unique elements
    return temp

# Create a list of strings 'text_str' with duplicate words
text_str = ["Python", "Exercises", "Practice", "Solution", "Exercises"]

# Print a message indicating the original list of strings
print("Original String:")
# Print the contents of 'text_str'
print(text_str)

# Remove duplicate words from the list of strings using the 'unique_list' function
print("\nAfter removing duplicate words from the said list of strings:")
# Call the 'unique_list' function with 'text_str', then print the result
print(unique_list(text_str))
