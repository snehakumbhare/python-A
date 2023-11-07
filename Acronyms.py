#Create Acronyms using Python
# ‘a’ to store the acronym of a phrase.

user_input = str(input("Enter a Phrase: "))
text = user_input.split()
a = " "
for i in text:
    a = a+str(i[0]).upper()
print(a)
