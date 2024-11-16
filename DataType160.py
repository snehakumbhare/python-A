#Python: Remove first specified number of elements from a given list satisfying a condition

#Write a  Python program to remove the first specified number of elements from a given list satisfying a condition.

#Remove the first 4 number of even numbers from the following list:
#[3,10,4,7,5,7,8,3,3,4,5,9,3,4,9,8,5]

#Output:
#[3, 7, 5, 7, 3, 3, 5, 9, 3, 4, 9, 8, 5]

# Define a function called condition_match that checks if a number is even.
def condition_match(x):
    return ((x % 2) == 0)

# Define a function called remove_items_con that takes a list 'data' and an integer 'N' as input.
def remove_items_con(data, N):
    # Initialize a counter variable 'ctr' to 1.
    ctr = 1
    
    # Create an empty list called 'result' to store the filtered elements.
    result = []
    
    # Iterate through the elements 'x' in the 'data' list.
    for x in data:
        # Check if the counter 'ctr' is greater than 'N' or if 'x' does not meet the condition of being even.
        if ctr > N or not condition_match(x):
            # If the condition is met, add 'x' to the 'result' list.
            result.append(x)
        else:
            # If the condition is not met, increment the counter 'ctr' by 1.
            ctr = ctr + 1
    
    # Return the 'result' list containing elements that meet the filtering criteria.
    return result

# Create a list 'nums' containing integer values.
nums = [3, 10, 4, 7, 5, 7, 8, 3, 3, 4, 5, 9, 3, 4, 9, 8, 5]

# Define the integer 'N' for the filtering condition.
N = 4

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Print a message indicating the purpose of the code.
print("\nRemove first 4 even numbers from the said list:")

# Call the 'remove_items_con' function to filter the list and remove the first 4 even numbers, then print the result.
print(remove_items_con(nums, N)) 
