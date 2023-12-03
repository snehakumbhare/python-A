#Python Program to Replace First Vowel With ‘-‘ in String15
def replace_vowel(string):
    vowels = "AEIOUaeiou"
    for i in range(len(string)):
        if string[i] in vowels:
            string = string[:i] + '-' + string[i+1:]
            break
    return string

string = input("Please enter a string: ")
print("Original String:", string)
print("Modified String:", replace_vowel(string)) 