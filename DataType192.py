#Python: Remove all strings from a given list of tuples

#Write a Python program to remove all strings from a given list of tuples.
# Define a function called 'test' that removes strings from a list of tuples.
def test(list1):
    # Create a list comprehension that processes each tuple in the input list.
    # Within each tuple, create a new tuple that contains values that are not strings.
    result = [tuple(v for v in i if not isinstance(v, str)) for i in list1]
    return list(result)  # Return the resulting list of tuples.

# Create a list of tuples 'marks', where each tuple contains numbers and strings.
marks = [(100, 'Math'), (80, 'Math'), (90, 'Math'), (88, 'Science', 89), (90, 'Science', 92)]

# Print a message indicating the original list of tuples.
print("\nOriginal list:")
# Print the original list 'marks'.
print(marks)

# Print a message indicating the result after removing strings from the list of tuples.
print("\nRemove all strings from the said list of tuples:")
# Call the 'test' function with 'marks' and print the result.
print(test(marks))
