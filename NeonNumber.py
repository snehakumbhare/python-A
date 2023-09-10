#WAP to check whether the given number is Neon or not
n= int(input("Enter a number:"))
sqr = n*n #square of num
sumOfDigit = 0

#calculating sum of digits of sqr
while sqr>0:
    sumOfDigit =sumOfDigit + sqr%10
    sqr = sqr//10

if (n == sumOfDigit):
    print(f"{n} is neon number")
else:
    print(f"{n} is not a neon number")
