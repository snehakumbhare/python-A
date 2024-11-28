#Python: Remove the last N number of elements from a given list
#Write a  Python program to remove the last N number of elements from a given list.
# Define a function called 'remove_last_n' that removes the last 'N' elements from a list 'nums'.
def remove_last_n(nums, N):
    # Slice the list 'nums' to exclude the last 'N' elements and create a new list 'result'.
    result = nums[:len(nums)-N]
    return result

# Create a list 'nums' containing integer values.
nums = [2, 3, 9, 8, 2, 0, 39, 84, 2, 2, 34, 2, 34, 5, 3, 5]

# Print a message indicating the original list.
print("Original lists:")
print(nums)

# Set the value 'N' to 3 and print a message indicating the intention to remove the last 'N' elements from the list.
N = 3
print("\nRemove the last", N, "elements from the said list:")

# Call the 'remove_last_n' function to remove the last 3 elements from the list 'nums' and print the result.
print(remove_last_n(nums, N))

# Set the value 'N' to 5 and print a message indicating the intention to remove the last 'N' elements from the list.
N = 5
print("\nRemove the last", N, "elements from the said list:")

# Call the 'remove_last_n' function to remove the last 5 elements from the list 'nums' and print the result.
print(remove_last_n(nums, N))

# Set the value 'N' to 1 and print a message indicating the intention to remove the last 'N' element from the list.
N = 1
print("\nRemove the last", N, "element from the said list:")

# Call the 'remove_last_n' function to remove the last element from the list 'nums' and print the result.
print(remove_last_n(nums, N))

