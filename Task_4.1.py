#Basic Calculator

#Funtion Definition
def addition(num1, num2):
    return num1 + num2

def subtraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return " Invalid Input Cannot Divide "
    return num1 / num2

#User input
number1 = int(input("Enter the First Number: "))
number2 = int(input("Enter the First Number: "))

#Operation Selection
operation = input("Choose an operation (+, -, *, /): ")

#Perform Calculation
if operation == '+':
 result = addition(number1, number2)
elif operation == '-':
 result = subtraction(number1, number2)
elif operation == '*':
 result = multiplication(number1, number2)
elif operation == '/':
 result = division(number1, number2)
else:
 result = "Invalid Operation"
 
print("The result is:",result)

    
