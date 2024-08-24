#Python: Create a 3X3 grid with numbers
#Write a  Python program to create a 3X3 grid with numbers.
nums = []
for i in range(3):
    nums.append([])
    for j in range(1, 4):
        nums[i].append(j)
print("3X3 grid with numbers:")
print(nums) 
