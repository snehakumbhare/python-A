#Python program to calculate the power using ‘while-loop’25
base = int(input("Enter the value for base :"))
exponent = int(input("Enter the value for exponent :"))
result=1;
print(base,"to power ",exponent,"=",end = ' ')
#using while loop with a condition that come out of while loop if exponent is 0
while exponent != 0:
    result = base * result
    exponent-=1
print(result)
#Enter the value for base :5
#Enter the value for exponent :4
#5 to power  4 = 625