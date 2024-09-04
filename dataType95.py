#Python: Sort each sublist of strings in a given list of lists
#Write a Python program to sort each sublist of strings in a given list of lists.
# Define a function 'sort_sublists' that sorts each sublist in 'input_list'
def sort_sublists(input_list):
    # Use the 'map' function to sort each sublist in 'input_list' and convert the result to a list
    result = list(map(sorted, input_list))
    return result

# Create a list 'color1' containing sublists of colors
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]

# Print a message indicating the original list
print("\nOriginal list:")
# Print the contents of 'color1'
print(color1)
# Print a message indicating the sorted sublists of the list
print("\nAfter sorting each sublist of the said list of lists:")
# Call the 'sort_sublists' function with 'color1' and print the result
print(sort_sublists(color1))
