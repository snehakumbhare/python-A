#Python: Count the number of elements in a list within a specified range
#Write a Python program to count the number of elements in a list within a specified range.
# Define a function named 'count_range_in_list' that counts the number of elements within a specified range
def count_range_in_list(li, min, max):
    # Initialize a counter 'ctr' to keep track of the count
    ctr = 0

    # Iterate through the elements 'x' in the input list 'li'
    for x in li:
        # Check if 'x' falls within the specified range [min, max]
        if min <= x <= max:
            # If 'x' is within the range, increment the counter 'ctr'
            ctr += 1

    # Return the final count of elements that fall within the range
    return ctr

# Define a list 'list1' containing numeric elements
list1 = [10, 20, 30, 40, 40, 40, 70, 80, 99]

# Call the 'count_range_in_list' function with 'list1' and the range [40, 100], and print the result
print(count_range_in_list(list1, 40, 100))

# Define another list 'list2' containing character elements
list2 = ['a', 'b', 'c', 'd', 'e', 'f']

# Call the 'count_range_in_list' function with 'list2' and the range ['a', 'e'], and print the result
print(count_range_in_list(list2, 'a', 'e')) 
