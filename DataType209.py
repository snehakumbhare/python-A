#Python: Compute the sum of non-zero groups (separated by zeros) of a given list of numbers

#Write a  Python program to compute the sum of non-zero groups (separated by zeros) of a given list of numbers.

# Define a function 'test' that computes the sum of non-zero groups separated by zeros in a list.
def test(lst):
    # Initialize an empty list 'result' to store the sums of non-zero groups.
    result = []
    # Initialize a variable 'ele_val' to keep track of the current group's sum.
    ele_val = 0
    
    # Iterate through the elements in the input list 'lst'.
    for digit in lst:
        # Check if the current digit is zero.
        if digit == 0:
            # If 'ele_val' is not zero (meaning the end of a non-zero group),
            # append it to the 'result' list and reset 'ele_val' to zero.
            if ele_val != 0:
                result.append(ele_val)
                ele_val = 0
        else:
            # Add the current digit to the 'ele_val' to accumulate the group's sum.
            ele_val += digit
    
    # If 'ele_val' is greater than zero (meaning there's a non-zero group at the end of the list),
    # append it to the 'result' list.
    if ele_val > 0:
        result.append(ele_val)
    
    return result

# Define a list of numbers 'nums'.
nums = [3, 4, 6, 2, 0, 0, 0, 0, 0, 0, 6, 7, 6, 9, 10, 0, 0, 0, 0, 0, 7, 4, 4, 0, 0, 0, 0, 0, 0, 5, 3, 2, 9, 7, 1, 0, 0, 0]

# Print a message indicating the original list.
print("\nOriginal list:")
# Print the original list of numbers 'nums'.
print(nums)

# Print a message indicating the purpose of the following lines of code.
print("\nCompute the sum of non-zero groups (separated by zeros) of the said list of numbers:")
# Call the 'test' function to compute the sums of non-zero groups in 'nums' and print the result.
print(test(nums)) 
