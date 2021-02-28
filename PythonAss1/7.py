#Create a list with at least 10 elements having integer values in it;        Print all elements        Perform slicing operations        Perform repetition with * operator        Perform concatenation with other list.

myList = ['one', 2, 3.14, [1,'two',(2017,2018)], ('python', 'hello')]
print('the elements in list are',myList)
print('\niterating through the elements in list')
for item in myList:
    print(item)

#slicing
print('\nThe first item in list is: ',myList[0])
print('\nThe elements at start index 1, step 0 and endindex 5 are: ',myList[1:5])
print('\nThe elements at start index -2, step -1 and endindex 2 are: ',myList[-2:-5:-1])

#repetition
myList2 = ['^']*3
print('\nthe new list with items repeated [\'^\'] 3 times is:',myList2)

#concatenation
myList3 = ['Hello', 'I', 'love', 'Python', 'programming']
newList = myList2 + myList3
print('\nThe concatenation of string myList2 and myList3 is:',newList)
