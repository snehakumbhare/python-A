#Python: Round every number of a given list of numbers and print the total 
#sum multiplied by the length of the list

#Write a  Python program to round every number in a given list of numbers and
#print the total sum multiplied by the length of the list.
# Create a list 'nums' containing floating-point numbers
nums = [22.4, 4.0, -16.22, -9.10, 11.00, -12.22, 14.20, -5.20, 17.50]

# Print a message indicating the original list
print("Original list: ", nums)

# Print a message indicating the result
print("Result:")

# Calculate the length of the 'nums' list and store it in the 'lenght' variable
lenght = len(nums)

# Calculate the sum of the rounded values in 'nums' using the map function,
# and then multiply the sum by the length of the list 'lenght'
print(sum(list(map(round, nums)) * lenght)) 
