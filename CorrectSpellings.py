#Correct Spellings using Python
#pip install pyspellchecker in your command prompt or terminal

from spellchecker import SpellChecker
corrector = SpellChecker()
word = input("Enter a Word : ")
if word in corrector:
    print("Correct")
else:
    correct_word = corrector.correction(word)
    print("Correct Spelling is ", correct_word)
