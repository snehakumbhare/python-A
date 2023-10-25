#Remove Cuss Words using Python
#pip install better_profanity

from better_profanity import profanity
text = "Please leave me alone and just piss off"
text = "Why am I doing all the fucking work?"
text = "He’s so fucking stupid!"

censored = profanity.censor(text)
print(censored)
