#Using loop structures print numbers from 1 to 100.  and using the same loop print numbers from 100 to 1 (reverse printing) a) By using For loop  b) By using while loop c) Let mystring ="Hello world"                                                                                                   print each character of mystring in to separate line using appropriate loop structure.

print("\nPrint numbers using for loop")
for num in range(0,100):
    print(num+1,"   ",100-num)

print()
print("\nPrint numbers using while loop")
startNum = 0
while startNum<100:
    print(startNum+1,"   ",100-startNum)
    startNum += 1

print("\nPrint each character of string in to separate line using appropriate loop structure.")
myString = "Hello world"
i=0
while i<len(myString):
    print(myString[i])
    i += 1

