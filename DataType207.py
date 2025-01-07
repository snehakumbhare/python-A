#Python: Sum a list of numbers

#Sum a list of numbers. Write a  Python program to sum the first number with the second and divide it by 2, then sum the second with the third and divide by 2, and so on.
#Equation: (element 0 + element 1) / 2, (element 1 + element 2) / 2, ... etc.
# Define a function 'test' that calculates the average of adjacent elements in a list.
def test(list1):
    # Use a list comprehension to iterate over adjacent elements in 'list1'.
    # Calculate the average of each pair of adjacent elements and store the results in a list.
    result = [(x + y) / 2.0 for (x, y) in zip(list1[:-1], list1[1:])]
    return list(result)

# Define a list of numbers 'nums'.
nums = [1, 2, 3, 4, 5, 6, 7]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list of numbers 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nSum the said list of numbers:")
# Call the 'test' function to calculate the averages of adjacent elements in 'nums' and print the result.
print(test(nums))

# Define another list of numbers 'nums'.
nums = [0, 1, -3, 3, 7, -5, 6, 7, 11]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list of numbers 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nSum the said list of numbers:")
# Call the 'test' function to calculate the averages of adjacent elements in 'nums' and print the result.
print(test(nums)) 
