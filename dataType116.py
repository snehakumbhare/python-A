#Python: Sort a list of lists by a given index of the inner list
#Write a  Python program to sort a list of lists by a given index of the inner list.
# Import the 'itemgetter' function from the 'operator' module
from operator import itemgetter

# Define a function 'index_on_inner_list' that sorts a list of lists based on a given index of the inner lists
def index_on_inner_list(list_data, index_no):
    # Use the 'sorted' function with 'itemgetter' to sort the list by the specified index
    result = sorted(list_data, key=itemgetter(index_no))
    return result

# Create a list 'students' with tuples representing student data
students = [('Sachin', 98, 99), ('Rajveer', 97, 96), ('Rudra', 91, 94), ('Bhumi', 94, 98)] 
# Print a message indicating the original list
print("Original list:")
# Print the contents of 'students'
print(students)

# Set the index number to 0
index_no = 0
# Print a message indicating the sorting by a given index
print("\nSort the said list of lists by a given index", "( Index =", index_no, ") of the inner list")
# Call the 'index_on_inner_list' function with 'students' and index_no, then print the result
print(index_on_inner_list(students, index_no))

# Set the index number to 2
index_no = 2
# Print a message indicating the sorting by a given index
print("\nSort the said list of lists by a given index", "( Index =", index_no, ") of the inner list")
# Call the 'index_on_inner_list' function with 'students' and index_no, then print the result
print(index_on_inner_list(students, index_no)) 
