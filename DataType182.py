#Python: Calculate the maximum and minimum sum of a sublist in a given list of lists

#Write a  Python program to calculate the maximum and minimum sum of a sublist in a given list of lists.

# Define a function called 'max_min_sublist' that finds the sublist with the maximum and minimum sums in a list of lists.
def max_min_sublist(lst):
    max_result = (max(lst, key=sum))  # Find the sublist with the maximum sum using the 'max' function and the 'sum' key.
    min_result = (min(lst, key=sum))  # Find the sublist with the minimum sum using the 'min' function and the 'sum' key.
    return max_result, min_result  # Return both the sublist with the maximum and minimum sums.

# Create a list of lists 'nums', where each sublist contains integers.
nums = [[1, 2, 3, 5], [2, 3, 5, 4], [0, 5, 4, 1], [3, 7, 2, 1], [1, 2, 1, 2]]

# Print a message indicating the original list of lists.
print("Original list:")
print(nums)

# Call the 'max_min_sublist' function with 'nums' and store the results for maximum and minimum sum sublists.
result = max_min_sublist(nums)

# Print a message indicating the maximum sum of a sublist in the list of lists.
print("\nMaximum sum of sub list of the said list of lists:")
# Print the sublist with the maximum sum.
print(result[0])

# Print a message indicating the minimum sum of a sublist in the list of lists.
print("\nMinimum sum of sub list of the said list of lists:")
# Print the sublist with the minimum sum.
print(result[1]) 
