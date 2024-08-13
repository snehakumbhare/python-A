#Python: Decode a run-length encoded given list
#Write a  Python program to decode a run-length message.
# Define a function 'decode' that takes a list 'alist' as input
def decode(alist):
    # Define a nested function 'aux' that processes individual elements or sublists
    def aux(g):
        # Check if the element 'g' is a list
        if isinstance(g, list):
            # If it is a list, return a tuple with the element at index 1 and a range of length 'g[0]'
            return [(g[1], range(g[0]))]
        else:
            # If 'g' is not a list, return a tuple with 'g' and a range of length 1
            return [(g, [0])]
    
    # Use list comprehensions to decode the run-length encoded 'alist'
    return [x for g in alist for x, R in aux(g) for i in R]

# Create a list 'n_list' containing a run-length encoded representation
n_list = [[2, 1], 2, 3, [2, 4], 5, 1]

# Print a message indicating the original encoded list
print("Original encoded list:")
# Print the original encoded list
print(n_list)

# Print a message indicating the decoded list from the run-length encoded input
print("\nDecode a run-length encoded said list:")
# Call the 'decode' function with 'n_list' and print the result
print(decode(n_list)) 
