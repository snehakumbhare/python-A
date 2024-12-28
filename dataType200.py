#Python: Pair up the consecutive elements of a given list

#Write a  Python program to pair consecutive elements of a given list.
# Define a function 'pair_consecutive_elements' that pairs up consecutive elements in a list.
def pair_consecutive_elements(lst):
    # Use a list comprehension to iterate over each index 'i' in the range up to the second-to-last index.
    # For each 'i', create a sublist containing the elements at index 'i' and 'i + 1' in the original list.
    result = [[lst[i], lst[i + 1]] for i in range(len(lst) - 1)]
    return result

# Create a list 'nums' containing integers.
nums = [1, 2, 3, 4, 5, 6]

# Print a message indicating the original list.
print("Original lists:")
# Print the original list of integers.
print(nums)

# Print a message indicating the purpose of the following line of code.
print("Pair up the consecutive elements of the said list:")
# Call the 'pair_consecutive_elements' function to create pairs of consecutive elements in the list.
print(pair_consecutive_elements(nums))

# Create a list 'nums' containing integers.
nums = [1, 2, 3, 4, 5]

# Print a message indicating the original list.
print("\nOriginal lists:")
# Print the original list of integers.
print(nums)

# Print a message indicating the purpose of the following line of code.
print("Pair up the consecutive elements of the said list:")
# Call the 'pair_consecutive_elements' function to create pairs of consecutive elements in the list.
print(pair_consecutive_elements(nums)) 
