#Write a program to find given number is odd or Even

def is_even_number(x):
    if (x%2==0):
       print("",x,"is an even number")
    else:
       print("",x,"is an odd number")

num = int(input("Enter First Number: "))
is_even_number(num)