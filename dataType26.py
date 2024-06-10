#Python: Check whether two lists are circularly identical
#Write a Python program to check whether two lists are circularly identical.
# Define three lists: list1, list2, and list3, each containing a sequence of numbers
list1 = [10, 10, 0, 0, 10]
list2 = [10, 10, 10, 0, 0]
list3 = [1, 10, 10, 0, 0]

# Compare list1 and list2
print('Compare list1 and list2')

# Check if the string representation of list2 is present in the string representation of list1 repeated twice
# The result will be True if list2 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list2)) in ' '.join(map(str, list1 * 2)))

# Compare list1 and list3
print('Compare list1 and list3')

# Check if the string representation of list3 is present in the string representation of list1 repeated twice
# The result will be True if list3 is a subsequence of list1 repeated twice, otherwise False
print(' '.join(map(str, list3)) in ' '.join(map(str, list1 * 2))) 
