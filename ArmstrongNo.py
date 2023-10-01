n=int(input("Enter a number:"))
n1=n
n2=n
d=len(str(n1))           #typecasting to find the length
total=0

while (n!=0):
    rem=n%10              
    total=total+(rem**d)
    n=n//10               #updating n value
    
if (n2==total):
    print(f"{n2} is an armstrong number")
    
else:
    print(f"{n2} is not an armstrong number")

          
