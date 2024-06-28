#Python: Split a list based on first character of word
#Write a  Python program to split a list based on the first character of a word.
# Import the 'groupby' function from the 'itertools' module and the 'itemgetter' function from the 'operator' module
from itertools import groupby
from operator import itemgetter

# Define a list 'word_list' containing words
word_list = ['be', 'have', 'do', 'say', 'get', 'make', 'go', 'know', 'take', 'see', 'come', 'think',
             'look', 'want', 'give', 'use', 'find', 'tell', 'ask', 'work', 'seem', 'feel', 'leave', 'call']

# Use 'groupby' to group and sort the words in 'word_list' based on the first letter of each word
# Iterate through the groups and print the first letter and the words starting with that letter
for letter, words in groupby(sorted(word_list), key=itemgetter(0)):
    print(letter)
    for word in words:
        print(word)
