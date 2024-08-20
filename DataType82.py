#Python: Generate the combinations of n distinct objects taken from a list

#Write a  Python program to generate combinations of n distinct objects taken from the elements of a given list.

# Define a function 'combination' that generates combinations of 'n' distinct objects from 'n_list'
def combination(n, n_list):
    # Base case: If 'n' is less than or equal to 0, yield an empty list and return
    if n <= 0:
        yield []
        return
    
    # Iterate through the elements in 'n_list'
    for i in range(len(n_list)):
        # Take one element 'c_num' at a time starting from index 'i'
        c_num = n_list[i:i+1]
        
        # Recursively generate combinations of 'n-1' distinct objects from the remaining elements
        for a_num in combination(n-1, n_list[i+1:]):
            # Yield the current element 'c_num' combined with the combinations of 'n-1' elements 'a_num'
            yield c_num + a_num

# Create a list 'n_list' containing integers
n_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# Print a message indicating the original list
print("Original list:")
# Print the original list
print(n_list)

# Assign an integer 'n' with the value 2
n = 2

# Call the 'combination' function with 'n' and 'n_list' and store the generator in the 'result' variable
result = combination(n, n_list)

# Print a message indicating the combinations of 'n' distinct objects
print("\nCombinations of", n, "distinct objects:")

# Iterate through the generator and print each combination
for e in result:
    print(e)
