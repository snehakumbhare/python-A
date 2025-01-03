#Python: Remove additional spaces in a given list
#Write a  Python program to remove additional spaces from a given list.
# Define a function 'test' that removes additional spaces from the elements of a given list.
def test(lst):
    # Create an empty list 'result' to store the modified elements.
    result = []
    # Iterate through the elements of the input list 'lst'.
    for i in lst:
        # Remove extra spaces in the current element and store it in 'j'.
        j = i.replace(' ', '')
        # Append the modified element 'j' to the 'result' list.
        result.append(j)
    return result

# Define a list 'text' containing strings with extra spaces.
text = ['abc ', '  ', ' ', 'sdfds ', ' ', '     ', 'sdfds ', 'huy']

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list 'text'.
print(text)

# Print a message indicating the purpose of the following lines of code.
print("Remove additional spaces from the said list:")
# Call the 'test' function to remove extra spaces from the elements of 'text' and print the result.
print(test(text)) 
