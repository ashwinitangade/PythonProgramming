#Write a program to find the biggest of 3 numbers 

def maximum_of_three_numbers(x,y,z):
   if ((x > y) and (x > z)):
      print("",x," is the biggest number between",x,",",y,",",z)
   elif ((y>x) and (y>z)):
      print("",y," is the biggest number between",x,",",y,",",z)
   elif ((z>x) and (z>y)):
      print("",z," is the biggest number between",x,",",y,",",z)
   else:
      print("cannot determine")

num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))
maximum_of_three_numbers(num1, num2, num3)
