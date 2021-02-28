#Write a program to find the biggest of 4 numbers.    a) Read 4 numbers from user using Input statement.    b) extend the above program to find the biggest of 5 numbers. (PS: Use IF and IF & Else, If and ELIf, and Nested IF)


def readInputList(n):
    list = []
    for i in range(0, n):
        ele = int(input())
        list.append(ele) # adding the element
    return list

def function_max(myList):
    biggestNum = myList[0]
    if (myList[0]>myList[1] and myList[0]>myList[2] and myList[0]>myList[3]):
        biggestNum = myList[0]
    elif (myList[1]>myList[0] and myList[1]>myList[2] and myList[1]>myList[3]):
        biggestNum = myList[1]
    elif (myList[2]>myList[0] and myList[2]>myList[1] and myList[2]>myList[3]):
        biggestNum = myList[2]
    elif (myList[3]>myList[0] and myList[3]>myList[1] and myList[3]>myList[2]):
        biggestNum = myList[3]
    return biggestNum

def function_max2(myList):
    biggestNum = number_list[0]
    i=0
    for num in number_list:
        if num > biggestNum:
           biggestNum = num
    return biggestNum

print('\nPlease enter 4 numbers:')
number_list = readInputList(4)
print('\nthe total elements added',len(number_list))
print('\nThe biggest number in the list is:',function_max(number_list))

number_list.clear()
print('\n\nPlease enter 5 new numbers:')
number_list = readInputList(5)
print('\nThe biggest number in the list is:',function_max2(number_list))
