#Python: Takes two lists and returns True if they have at least one common member

#Write a  Python function that takes two lists and returns True if they have at least one common member.
# Define a function called 'common_data' that takes two lists, 'list1' and 'list2', as input
def common_data(list1, list2):
    # Initialize a variable 'result' to False to indicate no common elements initially
    result = False

    # Iterate through each element 'x' in 'list1'
    for x in list1:
        # Iterate through each element 'y' in 'list2'
        for y in list2:
            # Check if the current elements 'x' and 'y' are equal
            if x == y:
                # If there's a common element, set 'result' to True and return it
                result = True
                return result

# Call the 'common_data' function with two lists and print the result
print(common_data([1, 2, 3, 4, 5], [5, 6, 7, 8, 9]))
# Call the 'common_data' function with two lists and print the result
print(common_data([1, 2, 3, 4, 5], [6, 7, 8, 9])) 
