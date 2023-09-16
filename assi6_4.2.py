#Accept input from user -> score in 5 subjects like math, physics, history, english and chemistry. 
# calculate total score and percentage.


math = float(input('math: '))
physics= float(input('physics: '))
history= float(input('history: '))
english= float(input('english:'))
chemistry= float(input('chemistry'))

Total = math+physics+history+english+chemistry
Percentage =(Total/500)*100

print("Total marks:",Total)
print("Percentage:",Percentage)