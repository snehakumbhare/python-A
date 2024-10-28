#Python: Frequency of the elements in a given list of lists
#Write a Python program to get the frequency of elements in a given list of lists.
# Define a function 'count_elements_lists' that counts the frequency of elements in a list of lists
def count_elements_lists(nums):
    # Flatten the list of lists into a single list using a list comprehension
    nums = [item for sublist in nums for item in sublist]
    
    # Initialize an empty dictionary 'dic_data' to store element frequencies
    dic_data = {}
    
    # Iterate through the flattened list 'nums'
    for num in nums:
        # Check if the element 'num' is already in the dictionary
        if num in dic_data.keys():
            # If yes, increment the frequency count
            dic_data[num] += 1
        else:
            # If not, create a new entry in the dictionary with key 'num' and initial value 1
            key = num
            value = 1
            dic_data[key] = value
    
    # Return the dictionary containing element frequencies
    return dic_data

# Create a list of lists 'nums' representing a 2D matrix
nums = [
        [1, 2, 3, 2],
        [4, 5, 6, 2],
        [7, 8, 9, 5],
       ]    

# Print a message indicating the original list of lists
print("Original list of lists:")
# Print the contents of 'nums'
print(nums)

# Print a message indicating the operation to count the elements' frequencies
print("\nFrequency of the elements in the said list of lists:")
# Call the 'count_elements_lists' function with 'nums' and print the result
print(count_elements_lists(nums)) 
