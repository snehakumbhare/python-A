#Python: Replace the last element in a list with another list

#Write a  Python program to replace the last element in a list with another list.

# Define two lists 'num1' and 'num2' containing integers
num1 = [1, 3, 5, 7, 9, 10]
num2 = [2, 4, 6, 8]

# Update the last element of 'num1' (using slicing) to be the entire 'num2' list
# This effectively replaces the last element of 'num1' with the elements of 'num2'
num1[-1:] = num2

# Print the modified 'num1' list, which now contains the elements of both 'num1' and 'num2'
print(num1)
