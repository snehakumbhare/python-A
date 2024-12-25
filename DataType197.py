#Python: Compute the average of nth elements in a given list of lists with different lengths

#Write a Python program to compute the average of the n-th element in a given list of lists with different lengths.

# Import the 'itertools' module as 'it' for convenience.
import itertools as it

# Create a list of lists 'nums' with varying lengths.
nums = [[0, 1, 2],
       [2, 3, 4],
       [3, 4, 5, 6],
       [7, 8, 9, 10, 11],
       [12, 13, 14]]

# Print a message indicating the original list of lists.
print("Original list:")
# Print the original 'nums' list.
print(nums)

# Define a function 'get_avg' that calculates the average of a list, ignoring 'None' values.
def get_avg(x):
    # Remove 'None' values from the list 'x'.
    x = [i for i in x if i is not None]
    # Calculate the average of the remaining values.
    return sum(x, 0.0) / len(x)

# Use the 'zip_longest' function from 'itertools' to iterate over the 'nums' lists and calculate the average.
result = map(get_avg, it.zip_longest(*nums))

# Print a message indicating the average of the n-th elements in the list of lists with different lengths.
print("\nAverage of n-th elements in the said list of lists with different lengths:")
# Convert the 'result' to a list and print it.
print(list(result)) 
