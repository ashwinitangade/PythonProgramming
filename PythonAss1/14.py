#Write a program to create two list A & B such that List A contains Employee Id, List B contain Employee name (minimum 10 entries in each list) & perform following operation      a) Print all names on to screen      b) Read the index from the  user and print the corresponding name from both list.      c) Print the names from 4th position to 9th position      d) Print all names from 3rd position till end of the list      e) Repeat list elements by specified number of times (N- times, where N is entered by user)      f)  Concatenate two lists and print the output.      g) Print element of list A and B side by side.(i.e. List-A First element, List-B First element )

employeeNameList = ['Aarav', 'Amita','Biren','Cavin','Danny','Gopal','Hetal','Leena','Meena','Neena','Vinay']
employeeIdList = ['123','234','345','456','567','678','789','890','247','347','457']

if len(employeeNameList) != len(employeeIdList):
    print('\nBoth the lists must have same length')
    exit(0)
for emp in employeeNameList:
   print(emp)

index = int(input("Enter index of employee: "))
if index > len(employeeNameList):
   print('\nPlease enter an index less than total number of employees which is: ',len(employeeNameList))
else:
    print('\nThe name of employee at index ',index,'is: ',employeeNameList[index],'and the id is: ',employeeIdList[index])
    
print('\nThe names from 4th position to 9th position are: ', employeeNameList[4:10:1])
print('\nThe names from 3rd position to 9th position are: ', employeeNameList[3::])

print('\n ')
repeatNum = int(input("Please enter by how many times you want to repeat the list: "))
newList = employeeNameList*repeatNum
print('\nThe new list is :',newList)

concatList = employeeNameList + employeeIdList
print('\nThe concatenated list of name and id is :',concatList)

print('\nName      EmpId')
for (name,empid) in zip(employeeNameList,employeeIdList):
    print('\n',name,'   ', empid)
