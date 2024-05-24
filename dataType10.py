#Python: Find the list of words that are longer than n from a given list of words
#Write a  Python program to find the list of words that are longer than n from a given list of words.
# Define a function called 'long_words' that takes an integer 'n' and a string 'str' as input
def long_words(n, str):
    # Create an empty list 'word_len' to store words longer than 'n' characters
    word_len = []

    # Split the input string 'str' into a list of words using space as the delimiter
    txt = str.split(" ")

    # Iterate through each word 'x' in the list of words 'txt'
    for x in txt:
        # Check if the length of the current word 'x' is greater than 'n'
        if len(x) > n:
            # If the word is longer than 'n' characters, add it to the 'word_len' list
            word_len.append(x)

    # Return the list of words longer than 'n' characters
    return word_len

# Call the 'long_words' function with an 'n' value of 3 and a string as input, and print the result
print(long_words(3, "The quick brown fox jumps over the lazy dog"))
