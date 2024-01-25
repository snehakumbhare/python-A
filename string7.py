#Python | Check for URL in a String

# Python code to find the URL from an input string
# Using the regular expression
import re
 
 
def Find(string):
 
    # findall() has been used
    # with valid conditions for urls in string
    regex = r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))"
    url = re.findall(regex, string)
    return [x[0] for x in url]
 
 
# Driver Code
string = 'url:https://www.hostinger.com/ https://www.microsoft.com/ and https://www.linux.org/'
print("Urls: ", Find(string))
