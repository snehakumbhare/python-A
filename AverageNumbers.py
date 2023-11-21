#Python program to find the average of numbers with explanations

size=int(input("Enter the number of elements you want in array: "))
arr=[]
#taking input of the list
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
#taking average of the elements of the list
avg=sum(arr)/size
print("Average of the array elements is ",avg)
#Enter the number of elements you want in array: 5
#Please give value for index 0: 9
#Please give value for index 1: 5
#Please give value for index 2: 7
#Please give value for index 3: 88
#Please give value for index 4: 21
#Average of the array elements is  26.0
