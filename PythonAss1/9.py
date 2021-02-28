#Write program to Add, Subtract, Multiply, Divide 2 Complex numbers.
import math

print('Add, Subtract, Multiply, Divide 2 Complex numbers.')
def add_complex_numbers( num1, num2):
    return num1 + num2
def sub_complex_numbers( num1, num2):
    return num1 - num2
def mul_complex_numbers( num1, num2):
    return num1 * num2
def div_complex_numbers( num1, num2):
    return num1 / num2
    
num1 = complex(5, 3)
num2 = complex(2, 1)
print( "Addtion is : ", add_complex_numbers(num1, num2))
print( "Substraction is : ", sub_complex_numbers(num1, num2))
print( "Multiplication is : ", mul_complex_numbers(num1, num2))
print( "Division is : ", div_complex_numbers(num1, num2))
