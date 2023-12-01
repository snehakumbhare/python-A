#Python program to calculate the power using ‘for-loop’
#taking 3 integer as input from the user

base = int(input("Enter the value for base :"))
exponent = int(input("Enter the value for exponent :"))
result=1;
print(base,"to power ",exponent,"=",end = ' ')
#using ‘for’ loop with ‘range’ function
for exponent in range(exponent, 0, -1):
    result *= base
print(result)

#Enter the value for base :5
#Enter the value for exponent :4
#5 to power  4 = 625
