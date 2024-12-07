#Python: Create the smallest possible number using the elements of a given list of integers
#Write a  Python program to create the smallest possible number using the elements of a given list of positive integers.
# Define a function 'create_smallest_number' that takes a list 'lst' as input.
def create_smallest_number(lst):
    # Check if all elements in the list are 0, return '0' if true.
    if all(val == 0 for val in lst):
        return '0'
    
    # Sort the elements in the list in ascending order based on a custom key.
    # The key is a lambda function that computes a string value for each element.
    # The length of the computed string is adjusted to ensure proper sorting.
    result = ''.join(sorted((str(val) for val in lst), reverse=False,
                      key=lambda i: i*( len(str(min(lst))) * 2 // len(i)))
                 )
    return result

# Create a list of positive integers.
nums = [3, 40, 41, 43, 74, 9]
print("Original list:")
print(nums)

# Call the 'create_smallest_number' function to find the smallest possible number
# using the elements of the list.
print("Smallest possible number using the elements of the said list of positive integers:")
print(create_smallest_number(nums))

# Repeat the process for two more sets of input data.
nums = [10, 40, 20, 30, 50, 60]
print("\nOriginal list:")
print(nums)
print("Smallest possible number using the elements of the said list of positive integers:")
print(create_smallest_number(nums))
nums = [8, 4, 2, 9, 5, 6, 1, 0]
print("\nOriginal list:")
print(nums)
print("Smallest possible number using the elements of the said list of positive integers:")
print(create_smallest_number(nums))
