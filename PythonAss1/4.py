#Write a program to find given number is odd or Even

def is_prime_number(num):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")

num = int(input("Enter a Number: "))
is_prime_number(num)
