#Python: Merge some list items in given list using index value

#Write a  Python program to merge some list items in a given list using the index value.

# Define a function called 'merge_some_chars' that merges characters in 
#a list 'lst' from index 'merge_from' to 'merge_to'.
def merge_some_chars(lst, merge_from, merge_to):
    # Create a new list 'result' as a reference to the input list 'lst'.
    result = lst
    # Join the characters from index 'merge_from' to 'merge_to' into a single 
    #string and replace the corresponding slice in 'result' with the merged string.
    result[merge_from:merge_to] = [''.join(result[merge_from:merge_to])]
    return result

# Create a list 'chars' containing character elements.
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Print a message indicating the original list.
print("Original list:")
print(chars)

# Set the values 'merge_from' to 2 and 'merge_to' to 4, and print a message indicating the intention to merge items from index 'merge_from' to 'merge_to' in the list.
merge_from = 2
merge_to = 4
print("\nMerge items from", merge_from, "to", merge_to, "in the said List:")

# Call the 'merge_some_chars' function to merge characters from index 2 to 4 in the list 'chars' and print the result.
print(merge_some_chars(chars, merge_from, merge_to))

# Create a new list 'chars' with the same elements.
chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

# Set the values 'merge_from' to 3 and 'merge_to' to 7, and print a message indicating the intention to merge items from index 'merge_from' to 'merge_to' in the list.
merge_from = 3
merge_to = 7
print("\nMerge items from", merge_from, "to", merge_to, "in the said List:")

# Call the 'merge_some_chars' function to merge characters from index 3 to 7 in the list 'chars' and print the result.
print(merge_some_chars(chars, merge_from, merge_to)) 
