#Python: Split a list every Nth element

#Write a  Python program to split a list every Nth element.

# Define a list 'C' containing alphabetic characters from 'a' to 'n'
C = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']

# Define a function 'list_slice' that takes a sequence 'S' and a 'step' value
# The function returns a list of slices from 'S' with a step of 'step'
def list_slice(S, step):
    return [S[i::step] for i in range(step)]

# Call the 'list_slice' function with the list 'C' and a step value of 3
# The function generates slices of 'C' with a step of 3 and returns a list of these slices
# Print the resulting list of slices
print(list_slice(C, 3))
