#Python: Find the second smallest number in a list
#Write a Python program to find the second smallest number in a list.
# Define a function named 'second_smallest' that takes a list of numbers 'numbers' as a parameter
def second_smallest(numbers):
    # Check if the length of the 'numbers' list is less than 2; return None in this case
    if len(numbers) < 2:
        return

    # Check if there are only two elements in the 'numbers' list, and they are the same; return None in this case
    if len(numbers) == 2 and numbers[0] == numbers[1]:
        return

    # Create an empty set 'dup_items' to store duplicate items and an empty list 'uniq_items' to store unique items
    dup_items = set()
    uniq_items = []

    # Iterate through the elements in the 'numbers' list
    for x in numbers:
        # Check if 'x' is not in 'dup_items'; if not, add it to 'uniq_items' and 'dup_items'
        if x not in dup_items:
            uniq_items.append(x)
            dup_items.add(x)

    # Sort the 'uniq_items' list in ascending order
    uniq_items.sort()

    # Return the second smallest item from the sorted 'uniq_items' list, which is at index 1
    return uniq_items[1]

# Call the 'second_smallest' function with different lists and print the results
print(second_smallest([1, 2, -8, -2, 0, -2]))
print(second_smallest([1, 1, 0, 0, 2, -2, -2]))
print(second_smallest([1, 1, 1, 0, 0, 0, 2, -2, -2]))
print(second_smallest([2, 2]))  # Edge case with two identical elements, returns None
print(second_smallest([2]))  # Edge case with a single element, returns None
