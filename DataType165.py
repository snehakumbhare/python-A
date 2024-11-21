#Python: Split a given list into specified sized chunks

#Write a  Python program to split a given list into specified-sized chunks.

# Define a function to split a list into equal-sized sublists of length 'n'
def split_list(lst, n):
    # Use list comprehension to create sublists of length 'n'
    result = list((lst[i:i+n] for i in range(0, len(lst), n)))
    # Return the list of sublists
    return result
# Create a list of numbers
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]
# Print the original list
print("Original list:")
print(nums)
# Define the size 'n' for splitting
n = 3
# Print a message about splitting the list into equal-sized sublists of size 'n'
print("\nSplit the said list into equal size", n)
# Call the split_list function with the list and size 'n' and print the result
print(split_list(nums, n))
# Repeat the process for different values of 'n'
n = 4
print("\nSplit the said list into equal size", n)
print(split_list(nums, n))
n = 5
print("\nSplit the said list into equal size", n)
print(split_list(nums, n))
