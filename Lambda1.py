#Lambda with if but without else in Python

# Lambda function with if but without else.
# square = lambda x : x*x if(x > 0) 
#print(square(6))

# Lambda function with if-else
square = lambda x : x*x if(x > 0) else None
 
print(square(4))

# Example of lambda function using if-else
mod = lambda x : x if(x >= 0) else -x
#mod = lambda x : x if(x >= 0)
print(mod(-1))

# Example of lambda function using if-else
max = lambda a, b : a if(a > b) else b
#max = lambda a, b : x if(a > b)
print(max(1, 2))
print(max(10, 2))
