#Python: Display each element vertically of a given list, list of lists
#Write a  Python program to display vertically each element of a given list, list of lists.
# Create a list 'text' containing string elements.
text = ["a", "b", "c", "d", "e", "f"]

# Print a message indicating the original list.
print("Original list:")
print(text)

# Print a message indicating the intention to display each element of the list vertically.
print("\nDisplay each element vertically of the said list:")

# Iterate through the elements in the list 'text' and print each element on a separate line.
for i in text:
    print(i)

# Create a list of lists 'nums' containing sublists of integers.
nums = [[1, 2, 5], [4, 5, 8], [7, 3, 6]]

# Print a message indicating the original list of lists.
print("Original list:")
print(nums)

# Print a message indicating the intention to display each element of the list of lists vertically.
print("\nDisplay each element vertically of the said list of lists:")

# Use 'zip' and tuple unpacking to iterate through and print the elements in sublists vertically.
for a, b, c in zip(*nums):
    print(a, b, c)
