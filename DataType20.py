#Python: Access the index of a list

#Write a  Python program to access the index of a list.

# Define a list 'nums' containing a sequence of numbers
nums = [5, 15, 35, 8, 98]
# Use a 'for' loop with 'enumerate' to iterate through 'nums' and obtain both the index and value of each element
for num_index, num_val in enumerate(nums):
    # Print the index and value of each element in 'nums'
    print(num_index, num_val)
