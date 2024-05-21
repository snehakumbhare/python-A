#Python: Remove duplicates from a list
#Write a Python program to remove duplicates from a list.
# Define a list 'a' with some duplicate and unique elements
a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40]

# Create an empty set to store duplicate items and an empty list for unique items
dup_items = set()
uniq_items = []

# Iterate through each element 'x' in the list 'a'
for x in a:
    # Check if the current element 'x' is not already in the set 'dup_items' (it's a duplicate check)
    if x not in dup_items:
        # If 'x' is not a duplicate, add it to the 'uniq_items' list
        uniq_items.append(x)
        # Add 'x' to the 'dup_items' set to mark it as a seen item
        dup_items.add(x)

# Print the set 'dup_items' which now contains the unique elements from the original list 'a'
print(dup_items) 
