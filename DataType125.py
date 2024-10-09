#Python: Calculate the product of the unique numbers of a given list

#Write a  Python program to calculate the product of the unique numbers in a given list.

# Define a function 'unique_product' that calculates the product of unique elements in a list
def unique_product(list_data):
    # Create a set 'temp' to store unique elements in the list
    temp = list(set(list_data))
    # Initialize a variable 'p' to store the product and set it to 1
    p = 1
    # Iterate through unique elements in 'temp'
    for i in temp:
        # Multiply the current element 'i' with 'p'
        p *= i
    # Return the product of unique elements
    return p

# Create a list 'nums' containing integers with some duplicates
nums = [10, 20, 30, 40, 20, 50, 60, 40]
# Print a message indicating the original list
print("Original List:", nums)
# Print a message indicating the product of unique numbers
print("Product of the unique numbers of the said list:", unique_product(nums)) 
