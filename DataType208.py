#Python: Count the number of groups of non-zero numbers separated by zeros of a given list of numbers

#Write a  Python program to count the number of groups of non-zero numbers separated by zeros in a given list of numbers.
# Define a function 'test' that counts the number of groups of non-zero numbers separated by zeros in a list.
def test(lst):
    # Initialize variables 'previous_digit' to store the previous digit and 'ctr' to count the groups.
    previous_digit = 0
    ctr = 0
    
    # Iterate through the elements in the input list 'lst'.
    for digit in lst:
        # Check if the previous digit was zero and the current digit is non-zero.
        if previous_digit == 0 and digit != 0:
            # Increment the group count.
            ctr += 1
        # Update the 'previous_digit' for the next iteration.
        previous_digit = digit
    
    return ctr

# Define a list of numbers 'nums'.
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 5, 9, 9, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list of numbers 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nNumber of groups of non-zero numbers separated by zeros of the said list:")
# Call the 'test' function to count the groups of non-zero numbers separated by zeros in 'nums' and print the result.
print(test(nums)) 
