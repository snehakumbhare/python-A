#Python: Concatenate element-wise three given lists
#Write a  Python program to concatenate element-wise three given lists.
# Define a function called 'concatenate_lists' that concatenates elements from three lists 'l1', 'l2', and 'l3' element-wise.
def concatenate_lists(l1, l2, l3):
    # Use a list comprehension with 'zip' to concatenate elements from each of the input lists.
    return [i + j + k for i, j, k in zip(l1, l2, l3)]

# Create three lists 'l1', 'l2', and 'l3' containing string elements.
l1 = ['0', '1', '2', '3', '4'] 
l2 = ['red', 'green', 'black', 'blue', 'white']
l3 = ['100', '200', '300', '400', '500'] 

# Print messages indicating the original lists.
print("Original lists:")
print(l1)
print(l2)
print(l3)

# Print a message indicating the intention to concatenate the three lists element-wise.
print("\nConcatenate element-wise three said lists:")

# Call the 'concatenate_lists' function to concatenate the lists 'l1', 'l2', and 'l3' element-wise and print the result.
print(concatenate_lists(l1, l2, l3))  
