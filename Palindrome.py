#wap to create a function to find palindrome number:

n=int(input("Enter a number:"))
n1=n
rev=0
while(n!=0):
    rem=n%10
    rev=(rev*10)+rem
    n=n//10
    
if(n1==rev):
    print(f"{n1} is a palindromic number")
    
else:
    print(f"{n1} is not a palindromic number")
