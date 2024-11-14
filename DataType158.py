#Python: Find the maximum and minimum values in a given list of tuples

#Write a  Python program to find the maximum and minimum values in a given list of tuples.
# Import the 'itemgetter' function from the 'operator' module.
from operator import itemgetter

# Define a function called max_min_list_tuples that takes a list of tuples 'class_students' as input.
def max_min_list_tuples(class_students):
    # Find the tuple with the maximum second element (index 1) in 'class_students' using 'itemgetter' and store it in 'return_max'.
    return_max = max(class_students, key=itemgetter(1))[1] 
    
    # Find the tuple with the minimum second element (index 1) in 'class_students' using 'itemgetter' and store it in 'return_min'.
    return_min = min(class_students, key=itemgetter(1))[1] 
    
    # Return the maximum and minimum values found in the list of tuples.
    return return_max, return_min

# Create a list of tuples 'class_students' where each tuple contains a class name and a student count.
class_students = [('V', 60), ('VI', 70), ('VII', 75), ('VIII', 72), ('IX', 78), ('X', 70)]

# Print a message indicating the original list with tuples.
print("Original list with tuples:")
print(class_students)

# Print a message indicating that the maximum and minimum values are being determined, and call the 'max_min_list_tuples' function.
print("\nMaximum and minimum values of the said list of tuples:")
print(max_min_list_tuples(class_students)) 
