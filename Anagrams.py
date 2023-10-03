#Write a program to check if the given strings are anagram or not.
#An anagram of a string is another string that contains same characters, only the order of characters can be different. 
#For example, “abcd” and “dabc” 
def check(s1, s2):
    
    if(sorted(s1)== sorted(s2)):
        print("The strings are anagrams.")
    else:
        print("The strings aren't anagrams.")        
        
s1 = input("Enter string1: ")

s2 = input("Enter string2: ")

check(s1, s2)

