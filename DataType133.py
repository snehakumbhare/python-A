#Python: Check common elements between two given list are in same order or not
#Write a  Python program to check if two lists have the same elements in them in same order or not.
# Define a function 'same_order' that checks if common elements in two lists are in the same order
def same_order(l1, l2):
    # Find the common elements between 'l1' and 'l2' using set intersection
    common_elements = set(l1) & set(l2)
    
    # Filter 'l1' to keep only elements present in 'common_elements'
    l1 = [e for e in l1 if e in common_elements]
    
    # Filter 'l2' to keep only elements present in 'common_elements'
    l2 = [e for e in l2 if e in common_elements]
    
    # Check if the filtered 'l1' and 'l2' are equal, meaning the common elements are in the same order
    return l1 == l2

# Create three lists 'color1', 'color2', and 'color3' with string values
color1 = ["red", "green", "black", "orange"]
color2 = ["red", "pink", "green", "white", "black"]
color3 = ["white", "orange", "pink", "black"]

# Print a message indicating the original lists
print("Original lists:")
# Print the contents of 'color1', 'color2', and 'color3'
print(color1)
print(color2)
print(color3)

# Test if common elements between 'color1' and 'color2' are in the same order
print("\nTest common elements between color1 and color2 are in the same order?")
# Call the 'same_order' function with 'color1' and 'color2', then print the result
print(same_order(color1, color2))

# Test if common elements between 'color1' and 'color3' are in the same order
print("\nTest common elements between color1 and color3 are in the same order?")
# Call the 'same_order' function with 'color1' and 'color3', then print the result
print(same_order(color1, color3))

# Test if common elements between 'color2' and 'color3' are in the same order
print("\nTest common elements between color2 and color3 are in the same order?")
# Call the 'same_order' function with 'color2' and 'color3', then print the result
print(same_order(color2, color3)) 
