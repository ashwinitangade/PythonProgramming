#Write program to perform following:      i) Check whether given number is prime or not.     ii) Generate all the prime numbers between 1 to N where N is given number.

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

def print_prime_numbers(num):
    print("Prime numbers:",end=' ')
    for n in range(1,num):
        for i in range(2,n):
            if(n%i==0):
               break
        else:
            print(n,end=' ')

numr=int(input("Enter range:"))
print_prime_numbers(numr)
print()
