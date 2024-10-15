#Python: Count the frequency of consecutive duplicate elements in a given list of numbers
#Write a  Python program to count the frequency of consecutive duplicate elements in a given list of numbers.
# Define a function 'count_dups' that counts consecutive duplicate elements and their frequencies
def count_dups(nums):
    # Initialize empty lists 'element' and 'freque' to store elements and their frequencies
    element = []
    freque = []

    # Check if 'nums' list is empty, and return empty lists 'element' and 'freque' if so
    if not nums:
        return element

    # Initialize a variable 'running_count' to track the frequency of consecutive elements
    running_count = 1

    # Iterate through the 'nums' list using a loop
    for i in range(len(nums) - 1):
        # Check if the current element is equal to the next element
        if nums[i] == nums[i + 1]:
            # If equal, increment 'running_count'
            running_count += 1
        else:
            # If not equal, append 'running_count' to 'freque' and the current element to 'element'
            freque.append(running_count)
            element.append(nums[i])
            # Reset 'running_count' to 1
            running_count = 1

    # Append the last 'running_count' and the last element to 'freque' and 'element'
    freque.append(running_count)
    element.append(nums[i + 1])

    # Return both 'element' and 'freque' as a tuple
    return element, freque

# Create a list 'nums' with consecutive duplicate elements
nums = [1, 2, 2, 2, 4, 4, 4, 5, 5, 5, 5]

# Print a message indicating the original list
print("Original list:")
# Print the contents of 'nums'
print(nums)

# Print a message indicating the operation to count consecutive duplicate elements and their frequencies
print("\nConsecutive duplicate elements and their frequency:")
# Call the 'count_dups' function with 'nums' and print the result
print(count_dups(nums))
