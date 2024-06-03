#Python: Difference between the two lists

#Write a  Python program to calculate the difference between the two lists.
# Define a list 'list1' containing numbers
list1 = [1, 3, 5, 7, 9]

# Define another list 'list2' containing different numbers
list2 = [1, 2, 4, 6, 7, 8]

# Calculate the difference between 'list1' and 'list2' by converting them to sets and subtracting the sets
diff_list1_list2 = list(set(list1) - set(list2))

# Calculate the difference between 'list2' and 'list1' by converting them to sets and subtracting the sets
diff_list2_list1 = list(set(list2) - set(list1))

# Concatenate the differences 'diff_list1_list2' and 'diff_list2_list1' to obtain a list of all unique differences
total_diff = diff_list1_list2 + diff_list2_list1

# Print the total difference, which represents elements that are unique to each list
print(total_diff)
