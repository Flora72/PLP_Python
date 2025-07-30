# i defined the functions for each operation
def add(x, y): return x + y
def subtract (x,y) : return x - y
def multiply (x,y) : return x * y
def divide (x,y) : return x / y if y != 0 else "Error: You cannot divide by zero"
def modulus (x,y) : return x % y
 
# I used a dictionary to create an operator map
operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
    '%': modulus
}

# the user is asked to input the first operand, operator and the 2nd operand 
number1 = float (input("Enter your first number:"))
operator = input("Enter a mathematical operator(-, +, *, / or %):")
number2 = float (input("Enter your second number"))

# the if logic will perform the computation
if operator in operations:
    result = operations[operator](number1, number2)
else:
    result = "Invalid operator"
# the result will be printed
print("Result is :", result)