#Python: Bigrams of words in a given list of strings

#Write a  Python program to generate Bigrams of words from a given list of strings.
# Define a function called 'bigram_sequence' that generates bigrams from a list of text sequences.
def bigram_sequence(text_lst):
    result = [a for ls in text_lst for a in zip(ls.split(" ")[:-1], ls.split(" ")[1:])]
    # Split each text sequence into words, generate bigrams, and flatten the list of bigrams.
    return result

# Create a list of text sequences 'text'.
text = ["Sum all the items in a list", "Find the second smallest number in a list"]

# Print a message indicating the original list of text sequences.
print("Original list:")
print(text)

# Call the 'bigram_sequence' function with 'text' and store the bigrams.
print("\nBigram sequence of the said list:")
# Print the list of bigrams generated from the text sequences.
print(bigram_sequence(text)) 
