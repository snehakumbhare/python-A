#Python: Create a multidimensional list with zeros
#Write a  Python program to create a multidimensional list (lists of lists) with zeros.
# Create an empty multidimensional list 'nums'
nums = []

# Loop over a range of 3 times to create 3 sublists
for i in range(3):
    # Append an empty sublist to 'nums' for each iteration
    nums.append([])
    
    # Loop over a range of 2 times to fill each sublist with 2 zeros
    for j in range(2):
        # Append a zero to the current sublist for each iteration
        nums[i].append(0)

# Print a message indicating the resulting multidimensional list
print("Multidimensional list:")

# Print the 'nums' list containing the structure of zeros
print(nums)
