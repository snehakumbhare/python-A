#Program to check given number representation is in binary or not

num = int(input("please give a number : "))
while(num>0):
    j=num%10
    if j!=0 and j!=1:
        print("num is not binary")
        break
    num=num//10
    if num==0:
        print("num is binary") 
        
#please give a number : 5
#num is not binary
#please give a number : 1
#num is binary
