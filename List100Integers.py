#Python: Find a list of one hundred integers between 0 and 999 which all differ by ten from one another

#Write a  Python program to test a list of one hundred integers between 0 and 999, which all differ by ten from one another. Return True otherwise False.

# Define a function named 'test' that takes a list 'li' as input
def test(li):
    # Check if all elements in 'li' are within the range [0, 999] and have a minimum absolute difference of 10
    # Also, ensure that all elements are distinct and there are exactly 100 unique elements in 'li'
    return all(i in range(1000) and abs(i - j) >= 10 for i in li for j in li if i != j) and len(set(li)) == 100

# Create a list 'nums' containing one hundred integers from 0 to 999 with a difference of 10 between each pair
nums = list(range(0, 1000, 10))

# Print the original list
print("Original list:")
print(nums)

# Print the result of the test function applied to the 'nums' list
print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
print(test(nums))

# Create a different list 'nums' containing one hundred integers from 0 to 999 with a difference of 20 between each pair
nums = list(range(0, 1000, 20))

# Print the original list
print("\nOriginal list:")
print(nums)

# Print the result of the test function applied to the modified 'nums' list
print("Check whether the said list contains one hundred integers between 0 and 999 which all differ by ten from one another:")
print(test(nums))
