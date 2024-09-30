#Python: Check if a substring presents in a given list of string values
#Write a  Python program to check if a substring appears in a given list of string values.
# Define a function 'find_substring' that checks if a substring is present in any of the strings in a list
def find_substring(str1, sub_str):
    # Use a generator expression and 'any' to check if 'sub_str' is in any of the strings in 'str1'
    if any(sub_str in s for s in str1):
        return True
    return False

# Create a list 'colors' with string values
colors = ["red", "black", "white", "green", "orange"]
# Print a message indicating the original list
print("Original list:")
# Print the contents of 'colors'
print(colors)

# Set the substring to search for
sub_str = "ack"
# Print a message indicating the substring to search
print("Substring to search:")
# Print the value of 'sub_str'
print(sub_str)
# Print a message indicating the operation to check for the presence of the substring
print("Check if a substring is present in the said list of string values:")
# Call the 'find_substring' function with 'colors' and 'sub_str', then print the result
print(find_substring(colors, sub_str))

# Set a different substring to search for
sub_str = "abc"
# Print a message indicating the new substring to search
print("Substring to search:")
# Print the value of 'sub_str'
print(sub_str)
# Print a message indicating the operation to check for the presence of the substring
print("Check if a substring is present in the said list of string values:")
# Call the 'find_substring' function with 'colors' and 'sub_str', then print the result
print(find_substring(colors, sub_str)) 
