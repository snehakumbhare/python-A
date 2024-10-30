#Python: Generate a number in a specified range except some specific numbers
#Write a  Python program to generate a number in a specified range except for some specific numbers.
## Import the 'choice' function from the 'random' module
from random import choice

# Define a function 'generate_random' that generates a random number within a specified range, excluding certain numbers
def generate_random(start_range, end_range, nums):
    # Generate a random number within the specified range, excluding numbers in the 'nums' list
    result = choice([i for i in range(start_range, end_range) if i not in nums])
    return result
   
# Define the start and end range for the first random number generation
start_range = 1
end_range = 10
nums = [2, 9, 10]

# Print a message indicating the operation to generate a number within the specified range except for specific numbers
print("\nGenerate a number in a specified range (1, 10) except [2, 9, 10]")
# Call the 'generate_random' function with the specified range and excluded numbers, then print the result
print(generate_random(start_range, end_range, nums))

# Define the start and end range for the second random number generation
start_range = -5
end_range = 5
nums = [-5, 0, 4, 3, 2]

# Print a message indicating the operation to generate a number within the specified range except for specific numbers
print("\nGenerate a number in a specified range (-5, 5) except [-5, 0, 4, 3, 2]")
# Call the 'generate_random' function with the specified range and excluded numbers, then print the result
print(generate_random(start_range, end_range, nums)) 
