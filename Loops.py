#x= [1,2,3]

#y=['a','b','c']

#Given two list x and, using list comprehension take the cross product of x and y-:

#output-:[(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]

x= [1,2,3]
y=['a','b','c']
# output-:[(1, 'a'), (1, 'b'), (1, 'c'), (2, 'a'), (2, 'b'), (2, 'c'), (3, 'a'), (3, 'b'), (3, 'c')]
l=[(i,j)for i in x for j in y]
print(l)
