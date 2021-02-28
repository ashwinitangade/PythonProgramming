#Write program to find the biggest and Smallest of N numbers.       PS: Use the functions to find biggest and smallest numbers.

def findBiggestNum(myList):
    biggestNum = number_list[0]
    i=0
    for num in number_list:
        if num > biggestNum:
           biggestNum = num
    return biggestNum

def findSmallestNum(myList):
    smallestNum = number_list[0]
    i=0
    for num in number_list:
        if num < smallestNum:
            smallestNum = num
    return smallestNum


input_string = input("Enter a list element separated by space ")
number_list  = input_string.split()
print('\nThe list of numbers entered is ',number_list)
print('\nThe biggest number in the list is:',findBiggestNum(number_list))
print('\nThe smallert number in the list is:',findSmallestNum(number_list))
