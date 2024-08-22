#Python: Round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5

#Write a  Python program to round the numbers in a given list, print the minimum and maximum numbers and multiply the numbers by 5. 
#Print the unique numbers in ascending order separated by space.
# Create a list 'nums' containing floating-point numbers
nums = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]

# Print a message indicating the original list
print("Original list:", nums)

# Use the 'map' function to round each number in 'nums' and store the result in 'numbers'
numbers = list(map(round, nums))

# Print the minimum value in the 'numbers' list
print("Minimum value: ", min(numbers))

# Print the maximum value in the 'numbers' list
print("Maximum value: ", max(numbers))

# Create a set from 'numbers' to remove duplicates, then sort and multiply each value by 5
# Store the result back in 'numbers'
numbers = sorted(map(lambda n: n * 5, set(numbers)))

# Print a message indicating the result
print("Result:")

# Iterate through the 'numbers' list and print each value separated by a space
for numb in numbers:
    print(numb, end=' ') 
