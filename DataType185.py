#Python: Convert a given decimal number to binary list

#Write a  Python program to convert a given decimal number to a binary list.
# Define a function called 'decimal_to_binary_list' that converts a decimal number to a binary list.
def decimal_to_binary_list(n):
    result = [int(x) for x in list('{0:0b}'.format(n))]
    # Convert the decimal number 'n' to a binary string, convert each digit to an integer, and store in a list.
    return result

# Set the value of 'n' to 8.
n = 8

# Print a message indicating the original number.
print("Original Number:", n)

# Call the 'decimal_to_binary_list' function with 'n' and print the result.
print("Decimal number (", n, ") to binary list:")
# Print the binary representation of the number 8 as a list.
print(decimal_to_binary_list(n))

# Set the value of 'n' to 45.
n = 45

# Print a message indicating the original number.
print("\nOriginal Number:", n)

# Call the 'decimal_to_binary_list' function with 'n' and print the result.
print("Decimal number (", n, ") to binary list:")
# Print the binary representation of the number 45 as a list.
print(decimal_to_binary_list(n))

# Set the value of 'n' to 100.
n = 100

# Print a message indicating the original number.
print("\nOriginal Number:", n)

# Call the 'decimal_to_binary_list' function with 'n' and print the result.
print("Decimal number (", n, ") to binary list:")
# Print the binary representation of the number 100 as a list.
print(decimal_to_binary_list(n)) 
