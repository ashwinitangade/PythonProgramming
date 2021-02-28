#Create a list of 5 names and check given name exist in the List.         a) Use membership operator (IN) to check the presence of an element.         b) Perform above task without using membership operator.         c) Print the elements of the list in reverse direction.

name_list = ['Aarav', 'Amita','Biren','Cavin','Danny']

myStr = input("Please enter a name to check if it exists in the list: ")
print()

print('Check using IN operator')
if myStr in name_list:
    print(myStr,' exists in the list')
else:
    print(myStr,' does not exist in the list')

print()
print('Check NOT using IN operator')
nameExists = False
for item in name_list:
    if item == myStr:
        nameExists = True
        print(myStr,' exists in the list')
if nameExists == False:
   print(myStr,' does not exist in the list')

reverse_list = name_list[::-1]
print('\nPrint list in the reverse order: ', reverse_list)

