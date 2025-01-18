#Python: Count of elements in each group from list based groups of elements

#Write a  Python program to group the elements of a list based on the given function and return the count of elements in each group.

#Use collections.defaultdict to initialize a dictionary.
#Use map() to map the values of the given list using the given function./li>
#Iterate over the map and increase the element count each time it occurs.
# Import the 'defaultdict' class from the 'collections' module.
from collections import defaultdict

# Define a function called 'count_by' that counts occurrences in a list based on a provided function.
def count_by(lst, fn=lambda x: x):
    # Create a defaultdict to store the count of each value.
    count = defaultdict(int)
    
    # Iterate over the values in the list after applying the provided function.
    for val in map(fn, lst):
        # Increment the count for the current value.
        count[val] += 1
    
    # Convert the 'count' defaultdict into a regular dictionary and return it.
    return dict(count)

# Import the 'floor' function from the 'math' module.
from math import floor

# Print the result of counting occurrences in a list of floating-point numbers using the 'floor' function.
print(count_by([6.1, 4.2, 6.3], floor)) 

# Print the result of counting occurrences in a list of strings using the 'len' function.
print(count_by(['one', 'two', 'three'], len)) 
