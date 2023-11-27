#Python Program to convert Decimal to Octal number

def decimal_to_octal(decimal):
    if decimal == 0:
        return ""
    quotient = decimal // 8
    remainder = decimal % 8
    return decimal_to_octal(quotient) + str(remainder)
    
decimal = int(input("Please Enter a decimal number: "))
octal = decimal_to_octal(decimal)
print("Octal number is ", octal, " for ", decimal)

#Please Enter a decimal number: 157
#Octal number is  235  for  157
