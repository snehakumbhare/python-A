#Python: Check whether a list contains a sublist

#Write a  Python program to check whether a list contains a sublist.

# Define a function named 'is_Sublist' that checks if list 's' is a sublist of list 'l'
def is_Sublist(l, s):
    sub_set = False  # Initialize a flag 'sub_set' to indicate whether 's' is a sublist of 'l

    # Check if 's' is an empty list; in this case, 's' is a sublist of any list
    if s == []:
        sub_set = True
    # Check if 's' is equal to 'l'; if so, 's' is a sublist of 'l
    elif s == l:
        sub_set = True
    # Check if the length of 's' is greater than the length of 'l'; 's' cannot be a sublist in this case
    elif len(s) > len(l):
        sub_set = False
    else:
        # Iterate through the elements of 'l'
        for i in range(len(l)):
            # Check if the current element in 'l' matches the first element in 's'
            if l[i] == s[0]:
                n = 1
                while (n < len(s)) and (l[i + n] == s[n]):
                    n += 1

                # If 'n' equals the length of 's', 's' is a sublist of 'l
                if n == len(s):
                    sub_set = True

    # Return the value of 'sub_set,' which indicates whether 's' is a sublist of 'l

    return sub_set

# Define list 'a,' 'b,' and 'c'
a = [2, 4, 3, 5, 7]
b = [4, 3]
c = [3, 7]

# Check if 'b' is a sublist of 'a' and print the result
print(is_Sublist(a, b))

# Check if 'c' is a sublist of 'a' and print the result
print(is_Sublist(a, c)) 
