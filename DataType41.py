#Python: Create multiple lists

#Write a  Python program to create multiple lists.
#Create an empty dictionary named 'obj'
obj = {}

# Iterate through the range of numbers from 1 to 20
for i in range(1, 21):
    # Create an empty list as the value and associate it with the string representation of the number 'i' as the key in the dictionary 'obj'
    obj[str(i)] = []

# Print the resulting dictionary 'obj'
print(obj) 
