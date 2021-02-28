#Repeat program 7 with Tuples (Take example from Tutorial)

myTuple = ('python', 1,[3.14, 5, 'one'])
print('the elements in tuple are',myTuple)
print('\nIterating through the elements in myTuple')
for item in myTuple:
    print(item)

#slicing
print('\nThe first item in tuple is: ',myTuple[0])
print('\nThe elements at start index 1, step 0 and endindex 3 are: ',myTuple[1:3])
print('\nThe elements at start index -2, step -1 and endindex 2 are: ',myTuple[-2:-5:-1])

#repetition
myTuple2 = ('^',)*3
print('\nthe new tuple with items repeated (\'^\') times is:',myTuple2)

#concatenation
myTuple3 = ('Hello', 'I', 'love', 'Python', 'programming')
newTuple = myTuple2 + myTuple3
print('\nThe concatenation of string myTuple2 and myTuple3 is:',newTuple)
