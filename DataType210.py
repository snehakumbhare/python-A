#Python: Remove an element from a given list

#Write a  Python program to remove an element from a given list.

# Create a list 'student' containing mixed data types (strings and integers).
student = ['Ricky Rivera', 98, 'Math', 90, 'Science']

# Print a message indicating the original list.
print("Original list:")

# Print the original list 'student'.
print(student)

# Print a message indicating the purpose of the following lines of code.
print("\nAfter deleting an element, using the index of the element:")

# Use the 'del' statement to remove the element at index 0 from the 'student' list.
del(student[0])

# Print the updated 'student' list after deleting the element.
print(student) 
