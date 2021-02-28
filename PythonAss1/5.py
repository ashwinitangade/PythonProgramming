
#Write a program to receive 5 command line arguments and print each argument separately. Example: >> python test.py arg1 arg2 arg3 arg4 arg5 a) From the above statement your program should receive arguments and print them each of them.  b) Find the biggest of three numbers, where three numbers are passed as command line arguments.

import sys

print('Number of arguments:', len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))

biggestNum = sys.argv[1]
for i in range(1, 4):
    if sys.argv[i] > biggestNum:
        biggestNum = sys.argv[i]
     
print("\nBiggest Num is : ",biggestNum)
