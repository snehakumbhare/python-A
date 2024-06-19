#Python: Generate all sublists of a list
#Write a  Python program to generate all sublists of a list.
# Import the 'combinations' function from the 'itertools' module, which is used to generate combinations

from itertools import combinations

# Define a function named 'sub_lists' that generates all possible sublists of a given list 'my_list'
def sub_lists(my_list):
    subs = []  # Create an empty list 'subs' to store the sublists

    # Iterate through the range of numbers from 0 to the length of 'my_list' + 1
    for i in range(0, len(my_list) + 1):
        # Use the 'combinations' function to generate all combinations of 'my_list' of length 'i'
        temp = [list(x) for x in combinations(my_list, i)]

        # Check if 'temp' contains any elements; if so, extend the 'subs' list with the generated sublists
        if len(temp) > 0:
            subs.extend(temp)

    return subs  # Return the list of generated sublists

# Define a list 'l1' containing numeric elements and another list 'l2' containing string elements
l1 = [10, 20, 30, 40]
l2 = ['X', 'Y', 'Z']

# Print the original list 'l1'
print("Original list:")
print(l1)

# Print a label indicating the start of sublist generation for 'l1'
print("Sublists of the said list:")

# Call the 'sub_lists' function with 'l1' and print the sublists of 'l1'
print(sub_lists(l1))

# Print a newline for separation
print("\nOriginal list:")
print(l2)

# Print a label indicating the start of sublist generation for 'l2'
print("Sublists of the said list:")

# Call the 'sub_lists' function with 'l2' and print the sublists of 'l2'
print(sub_lists(l2))
