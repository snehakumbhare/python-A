#Python: Merge two or more lists into a list of lists
#Write a Python program to merge two or more lists into a list of lists, combining elements from each of the input lists based on their positions.

#Merges two or more lists into a list of lists, combining elements from each of the input lists based on their positions.

#Use max() combined with a list comprehension to get the length of the longest list in the arguments.
#Use range() in combination with the max_length variable to loop as many times as there are elements in the longest list
#If a list is shorter than max_length, use fill_value for the remaining items (defaults to None)
#zip() and itertools.zip_longest() provide similar functionality to this snippet

# Define a function called 'merge_lists' that merges multiple lists into a list of lists.
def merge_lists(*args, fill_value=None):
    # Find the maximum length among all input lists.
    max_length = max([len(lst) for lst in args])
    result = []
    
    # Iterate over the indices up to the maximum length.
    for i in range(max_length):
        # Create a new list by taking elements from each input list at the same index,
        # or using the 'fill_value' if the index is out of bounds for any list.
        result.append([args[k][i] if i < len(args[k]) else fill_value for k in range(len(args))])
    
    return result

# Print a message indicating the result after merging lists into a list of lists.
print("After merging lists into a list of lists:")

# Call the 'merge_lists' function with three lists.
print(merge_lists(['a', 'b'], [1, 2], [True, False]))  

# Call the 'merge_lists' function with three lists, one of which is shorter.
print(merge_lists(['a'], [1, 2], [True, False]))  

# Call the 'merge_lists' function with three lists, using a custom 'fill_value'.
print(merge_lists(['a'], [1, 2], [True, False], fill_value='_'))
