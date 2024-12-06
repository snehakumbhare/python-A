#Python: Create the largest possible number using the elements of a given list of integers

#Write a  Python program to create the largest possible number using the elements of a given list of positive integers.
# Define a function called 'create_largest_number' that constructs the largest possible number from a list of integers.
def create_largest_number(lst):
    # Check if all elements in the list are zero.
    if all(val == 0 for val in lst):
        return '0'  # If all elements are zero, return '0'.

    # Use a sorting approach to create the largest number. Sort in reverse order based on custom comparison criteria.
    result = ''.join(sorted((str(val) for val in lst), reverse=True,
                  key=lambda i: i * (len(str(max(lst))) * 2 // len(i))))
    return result

# Create a list of positive integers 'nums'.
nums = [3, 40, 41, 43, 74, 9]

# Print a message indicating the original list of positive integers.
print("Original list:")
print(nums)

# Print a message indicating the largest possible number that can be created from the elements in 'nums'.
print("Largest possible number using the elements of the said list of positive integers:")
print(create_largest_number(nums))

# Create another list of positive integers 'nums'.
nums = [10, 40, 20, 30, 50, 60]

# Print a message indicating the original list of positive integers.
print("\nOriginal list:")
print(nums)

# Print a message indicating the largest possible number that can be created from the elements in the second 'nums' list.
print("Largest possible number using the elements of the said list of positive integers:")
print(create_largest_number(nums))

# Create a third list of positive integers 'nums'.
nums = [8, 4, 2, 9, 5, 6, 1, 0]

# Print a message indicating the original list of positive integers.
print("\nOriginal list:")
print(nums)

# Print a message indicating the largest possible number that can be created from the elements in the third 'nums' list.
print("Largest possible number using the elements of the said list of positive integers:")
print(create_largest_number(nums)) 
