#Python: Check if a given element occurs at least n times in a list
#Write a  Python program to check if a given element occurs at least n times in a list.
# Define a function called check_element_in_list that takes three arguments: 'lst' (list), 'x' (element to check), and 'n' (minimum occurrences).
def check_element_in_list(lst, x, n):
    # Initialize a variable 't' to 0.
    t = 0
    
    try:
        # Iterate 'n' times to check for 'x' in the list.
        for _ in range(n):
            # Find the index of 'x' in 'lst' starting from index 't'.
            t = lst.index(x, t) + 1
        
        # If 'x' is found at least 'n' times, return True.
        return True
    
    except ValueError:
        # If 'x' is not found 'n' times, return False.
        return False

# Create a list 'nums' containing integer values.
nums = [0, 1, 3, 5, 0, 3, 4, 5, 0, 8, 0, 3, 6, 0, 3, 1, 1, 0]

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Define 'x' and 'n' for the first check.
x = 3
n = 4

# Print a message indicating that we are checking if 'x' occurs at least 'n' times in the list.
print("\nCheck if", x, "occurs at least", n, "times in a list:")

# Call the 'check_element_in_list' function to check if 'x' occurs at least 'n' times and print the result.
print(check_element_in_list(nums, x, n))

# Define 'x' and 'n' for the second check.
x = 0
n = 5

# Print a message indicating that we are checking if 'x' occurs at least 'n' times in the list.
print("\nCheck if", x, "occurs at least", n, "times in a list:")

# Call the 'check_element_in_list' function to check if 'x' occurs at least 'n' times and print the result.
print(check_element_in_list(nums, x, n))

# Define 'x' and 'n' for the third check.
x = 8
n = 3

# Print a message indicating that we are checking if 'x' occurs at least 'n' times in the list.
print("\nCheck if", x, "occurs at least", n, "times in a list:")

# Call the 'check_element_in_list' function to check if 'x' occurs at least 'n' times and print the result.
print(check_element_in_list(nums, x, n))
