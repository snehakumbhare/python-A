#Python: Interleave multiple lists of the same length

#Write a  Python program to interleave multiple lists of the same length.

# Define a function 'interleave_multiple_lists' that interleaves elements from multiple lists
def interleave_multiple_lists(list1, list2, list3):
    # Use a list comprehension with 'zip' to interleave elements from 'list1', 'list2', and 'list3'
    result = [el for pair in zip(list1, list2, list3) for el in pair]
    return result

# Create three lists 'list1', 'list2', and 'list3' with integer values
list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = [10, 20, 30, 40, 50, 60, 70]
list3 = [100, 200, 300, 400, 500, 600, 700]

# Print a message indicating the original lists
print("Original list:")
print("list1:", list1)
print("list2:", list2)
print("list3:", list3)

# Print a message indicating the interleaved lists
print("\nInterleave multiple lists:")
# Call the 'interleave_multiple_lists' function with 'list1', 'list2', and 'list3' and print the result
print(interleave_multiple_lists(list1, list2, list3)) 
