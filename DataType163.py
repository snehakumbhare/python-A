#Python: Index of the first element which is greater than a specified element

#Write a  Python program to get the index of the first element that is greater than a specified element.
# Define a function called 'first_index' that finds the index of the first element in a list 'l1' greater than a given number 'n'.
def first_index(l1, n):
    # Use the 'enumerate' function to iterate over the list 'l1' along with its indices.
    # Find the first element in the list greater than 'n' and return its index.
    return next(a[0] for a in enumerate(l1) if a[1] > n)

# Create a list 'nums' containing integer values.
nums = [12, 45, 23, 67, 78, 90, 100, 76, 38, 62, 73, 29, 83]

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Set the value 'n' to 73 and print a message indicating the index of the first element greater than 'n' in the list.
n = 73
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))

# Set the value 'n' to 21 and print a message indicating the index of the first element greater than 'n' in the list.
n = 21
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))

# Set the value 'n' to 80 and print a message indicating the index of the first element greater than 'n' in the list.
n = 80
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n))

# Set the value 'n' to 55 and print a message indicating the index of the first element greater than 'n' in the list.
n = 55
print("\nIndex of the first element which is greater than", n, "in the said list:")
print(first_index(nums, n)) 
