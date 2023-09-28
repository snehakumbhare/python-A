#Write a python program to calculate and print total ,average and 
# percentage of marks.(input five subjects say,Java,Python,ML,HTML,DS)

Java = float(input('Java: '))
Python= float(input('Python: '))
ML = float(input('ML: '))
HTML = float(input('HTML:'))
DS = float(input('DS'))

total = Java+Python+ML+HTML+DS
average = total / 5
percentage =(total/500)*100

print("Total marks:",total)
print("Average marks:", average)
print("Percentage:",percentage)