#Python: Extract the nth element from a given list of tuples

#Write a  Python program to extract the nth element from a given list of tuples.

# Define a function 'extract_nth_element' that extracts the nth element from each tuple in a list
def extract_nth_element(test_list, n):
    # Use list comprehension to extract the nth element (index n) from each tuple in the list
    result = [x[n] for x in test_list]
    return result

# Create a list 'students' containing tuples with student names and their exam scores
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 

# Print a message indicating the original list
print("Original list:")
# Print the contents of the 'students' list
print(students)

# Set the value of 'n' to 0
n = 0
# Print a message indicating the extraction of the 0th element from each tuple
print("\nExtract nth element (n =", n, ") from the said list of tuples:")
# Call the 'extract_nth_element' function with 'students' and 'n', then print the result
print(extract_nth_element(students, n))

# Set the value of 'n' to 2
n = 2
# Print a message indicating the extraction of the 2nd element from each tuple
print("\nExtract nth element (n =", n, ") from the said list of tuples:")
# Call the 'extract_nth_element' function with 'students' and 'n', then print the result
print(extract_nth_element(students, n)) 
