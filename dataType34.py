#Python: Sieve of Eratosthenes method, for computing prime number
#Write a  Python program that uses the Sieve of Eratosthenes method to compute prime numbers up to a specified number.
# Define a function named 'prime_eratosthenes' that generates prime numbers using the Sieve of Eratosthenes algorithm
def prime_eratosthenes(n):
    prime_list = []  # Create an empty list to store prime numbers
    # Iterate through the numbers from 2 to 'n'
    for i in range(2, n+1):
        if i not in prime_list:
            # If 'i' is not in the 'prime_list,' it's a prime number; print it
            print(i)

            # Mark all multiples of 'i' as non-prime by adding them to 'prime_list'
            for j in range(i*i, n+1, i):
                prime_list.append(j)

# Call the 'prime_eratosthenes' function with 'n' set to 100 to generate prime numbers
# The function does not have a return value, so it prints the prime numbers directly
prime_eratosthenes(100)
