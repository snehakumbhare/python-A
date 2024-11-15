#Python: Append the same value /a list multiple times to a list/list-of-lists

#Write a  Python program to append the same value/a list multiple times to a list/list-of-lists.

# Print a message indicating the purpose of the code.
print("Add a value(7), 5 times, to a list:")

# Create an empty list 'nums'.
nums = []

# Extend the 'nums' list by adding the value '7' five times using the '+=' operator.
nums += 5 * ['7']

# Print the resulting 'nums' list after the addition.
print(nums)

# Create a list 'nums1' containing some integer values.
nums1 = [1, 2, 3, 4]

# Print a message indicating the purpose of the code.
print("\nAdd 5, 6 times, to a list:")

# Extend the 'nums1' list by adding the value '5' six times using the '+=' operator.
nums1 += 6 * [5]

# Print the resulting 'nums1' list after the addition.
print(nums1)

# Print a message indicating the purpose of the code.
print("\nAdd a list, 4 times, to a list of lists:")

# Create an empty list 'nums1'.
nums1 = []

# Extend the 'nums1' list by adding the list [1, 2, 5] four times using the '+=' operator.
nums1 += 4 * [[1, 2, 5]]

# Print the resulting 'nums1' list after the addition.
print(nums1)

# Create a list 'nums1' containing a single list [5, 6, 7].
nums1 = [[5, 6, 7]]

# Print a message indicating the purpose of the code.
print("\nAdd a list, 4 times, to a list of lists:")

# Extend the 'nums1' list by adding the list [1, 2, 5] four times using the '+=' operator.
nums1 += 4 * [[1, 2, 5]]

# Print the resulting 'nums1' list after the addition.
print(nums1) 
