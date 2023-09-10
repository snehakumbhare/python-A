#Create a function to find out Cube of given number
def cube(num):
    return num * num * num
 
num = int(input("Enter an any number : "))
 
cube1 = cube(num)
 
print("Cube of {} is {}".format(num, cube1))
