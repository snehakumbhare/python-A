#Python: Insert an element in a given list after every nth position
#Write a  Python program to insert an element in a given list after every nth position.
# Define a function called 'insert_elemnt_nth' that inserts an element 'ele' into a list 'lst' after every 'n' elements.
def insert_elemnt_nth(lst, ele, n):
    # Create an empty list 'result' to store the modified list.
    result = []
    # Iterate over the list with a step of 'n' using a range.
    for st_idx in range(0, len(lst), n):
        # Extend 'result' with the elements from the current slice of 'lst' and add 'ele'.
        result.extend(lst[st_idx:st_idx+n])
        result.append(ele)
    # Remove the last occurrence of 'ele' to correct any extra insertions.
    result.pop()
    return result

# Create a list 'nums' containing integer values.
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Print a message indicating the original list.
print("Original list:")
print(nums)

# Set the element 'i_ele' to 'a' and the insertion position 'i_ele_pos' to 2.
i_ele = 'a'
i_ele_pos = 2
print("\nInsert", i_ele, "in the said list after", i_ele_pos, "nd element:")

# Call the 'insert_elemnt_nth' function to insert 'i_ele' into 'nums' after every 2nd element and print the result.
print(insert_elemnt_nth(nums, i_ele, i_ele_pos))

# Set the element 'i_ele' to 'b' and the insertion position 'i_ele_pos' to 4.
i_ele = 'b'
i_ele_pos = 4
print("\nInsert", i_ele, "in the said list after", i_ele_pos, "th element:")

# Call the 'insert_elemnt_nth' function to insert 'i_ele' into 'nums' after every 4th element and print the result.
print(insert_elemnt_nth(nums, i_ele, i_ele_pos))  
