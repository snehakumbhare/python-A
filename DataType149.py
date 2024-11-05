#Python: All possible combinations of the elements of a given list
#Write a  Python program to get all possible combinations of the elements of a given list.
# Define a function 'combinations_list' to generate all possible combinations of a list's elements
def combinations_list(colors):
    # Base case: if the input list 'colors' is empty, return a list containing an empty list
    if len(colors) == 0:
        return [[]]
    result = []
    # Recursive case: for each element in the list, generate combinations with and without the element
    for el in combinations_list(colors[1:]):
        result += [el, el + [colors[0]]]
    return result

# Create a list 'colors' with elements
colors = ['orange', 'red', 'green', 'blue']

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'colors'
print(colors)

# Print a message indicating the operation to generate all possible combinations
print("\nAll possible combinations of the said list’s elements:")
# Call the 'combinations_list' function with 'colors' and print the result
print(combinations_list(colors)) 
