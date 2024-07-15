#Python: Compute the difference between two lists
#Write a  Python program to compute the difference between two lists.

# Import the 'Counter' class from the 'collections' module
from collections import Counter

# Define two lists 'color1' and 'color2' containing color names
color1 = ["red", "orange", "green", "blue", "white"]
color2 = ["black", "yellow", "green", "blue"]

# Create Counter objects 'counter1' and 'counter2' for each list to count the occurrences of color names
counter1 = Counter(color1)
counter2 = Counter(color2)

# Print the elements that are in 'counter1' but not in 'counter2' (Color1-Color2)
print("Color1-Color2: ", list(counter1 - counter2))

# Print the elements that are in 'counter2' but not in 'counter1' (Color2-Color1)
print("Color2-Color1: ", list(counter2 - counter1))
