#Python: Remove key values pairs from a list of dictionaries
#Write a  Python program to remove  key-value pairs from a list of dictionaries.
# Define a list 'original_list' containing dictionaries, where each dictionary has 'key1' and 'key2' as keys with corresponding values
original_list = [{'key1': 'value1', 'key2': 'value2'}, {'key1': 'value3', 'key2': 'value4'}]

# Print the original list 'original_list'
print("Original List: ")
print(original_list)

# Use a list comprehension to create a new list 'new_list'
# In the new list, each dictionary is filtered to include only key-value pairs where the key is not 'key1'
# This effectively removes the 'key1' key-value pair from each dictionary
new_list = [{k: v for k, v in d.items() if k != 'key1'} for d in original_list]

# Print the new list 'new_list'
print("New List: ")
print(new_list)
