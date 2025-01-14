#Python: Sort a given positive number in descending/ascending order
#Write a  Python program to sort a given positive number in descending/ascending order.
# Define a function called 'test_dsc' that takes an integer 'n' and returns the integer formed by its digits sorted in descending order.
def test_dsc(n):
    # Convert the integer 'n' to a string, sort its characters in descending order, and convert them back to an integer.
    return int(''.join(sorted(str(n), reverse=True)))
	
# Define a function called 'test_asc' that takes an integer 'n' and returns the integer formed by its digits sorted in ascending order.
def test_asc(n):
    # Convert the integer 'n' to a string, sort its characters in ascending order, and convert them back to an integer.
    return int(''.join(sorted(list(str(n)))[::1]))

# Assign an integer value to 'n'.
n = 134543
# Print a message indicating the original number.
print("Original Number: ", n)
# Calculate and print the descending order of the number using the 'test_dsc' function.
print("Descending order of the said number: ", test_dsc(n))
# Calculate and print the ascending order of the number using the 'test_asc' function.
print("Ascending order of the said number: ", test_asc(n))

# Assign another integer value to 'n'.
n = 43750973
# Print a message indicating the original number.
print("\nOriginal Number: ", n)
# Calculate and print the descending order of the number using the 'test_dsc' function.
print("Descending order of the said number: ", test_dsc(n))
# Calculate and print the ascending order of the number using the 'test_asc' function.
print("Ascending order of the said number: ", test_asc(n)) 
