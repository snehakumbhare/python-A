#Python code to perform right rotation on array (list) elements by two positions

#taking the input from the user to fix the array size

size=int(input("Enter the number of elements you want in array: "))
arr=[]

# adding elements to the array (list)
for i in range(0,size):
    elem=int(input("Please give value for index "+str(i)+": "))
    arr.append(elem)
for i in range(0,2):
# storing last element of the array (list) in temp variable
    temp=arr[size-1];
    for j in range(size-1,-1,-1):
        arr[j]=arr[j-1]
        
# making the last element of the array, the first element
    arr[0]=temp;
print("Array after performing right rotation :")
print(arr)
