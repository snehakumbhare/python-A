#Python Exercises: Check if each number is prime in a list of numbers

#Write a  Python program to check if each number is prime in a given list of numbers. Return True if all numbers are prime otherwise False.
# Define a function named 'test' that takes a list 'nums' as a parameter
def test(nums):
    # Use a generator expression to check if each number in 'nums' is prime, and return True if all are prime
    return all(is_prime(i) for i in nums)

# Define a function named 'is_prime' that checks if a number 'n' is prime
def is_prime(n):
    # Check if 'n' is equal to 1; if so, it's not prime
    if (n == 1):
        return False
    # Check if 'n' is equal to 2; if so, it's prime
    elif (n == 2):
        return True
    else:
        # Iterate through numbers from 2 to 'n' - 1
        for x in range(2, n):
            # If 'n' is divisible by 'x', it's not prime; return False
            if (n % x == 0):
                return False
        # If no divisors were found, 'n' is prime; return True
        return True

# Define a list 'nums' containing a sequence of numbers
nums = [0, 3, 4, 7, 9]
# Print the original list of numbers
print("Original list of numbers:")
print(nums)
# Check if each number in 'nums' is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with a different list of numbers
nums = [3, 5, 7, 13]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums))

# Reassign 'nums' with another list of numbers
nums = [1, 5, 3]
# Print the original list of numbers
print("\nOriginal list of numbers:")
print(nums)
# Check if each number in the new 'nums' list is prime and print the result
print("Check if each number is prime in the said list of numbers:")
print(test(nums)) 
