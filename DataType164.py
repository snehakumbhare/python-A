#Python: Get the items from a given list with specific condition
#Write a Python program to get items from a given list with specific conditions.

#Number of Items of the following list which are even and greater than 73
#[12,45,23,67,78,90,45,32,100,76,38,62,73,29,83]
#Output:
#5

# Define a function called 'first_index' that counts the number of elements in a list 'l1' that are even and greater than 45.
def first_index(l1):
    # Use a generator expression with 'sum' to count the elements in 'l1' that meet the specified conditions.
    return sum(1 for i in l1 if (i > 45 and i % 2 == 0))

# Create a list 'nums' containing integer values.
nums = [12, 45, 23, 67, 78, 90, 45, 32, 100, 76, 38, 62, 73, 29, 83]

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Set the value 'n' to 45 and print a message indicating the number of items in the list that are even and greater than 'n'.
n = 45
print("\nNumber of items of the said list which are even and greater than", n)
print(first_index(nums)) 
