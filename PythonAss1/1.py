#Write a program to Add, Subtract, Multiply, and Divide 2 numbers

def myadd(x, y):
    return x + y

def mysub(x, y):
    return x - y

def mymul(x, y):
    return x * y

def mydivide(x, y):
    return x / y

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
op = input("Enter any of these char for specific operation +,-,*,/: ")

result = 0
if op == '+':
    result = myadd(num1,num2)
elif op == '-':
    result = mysub(num1,num2)
elif op == '*':
    result = mymul(num1,num2)
elif op == '/':
    result = mydivide(num1,num2)
else:
    print("Input character is not recognized!")

print(num1, op , num2, ":", result)
