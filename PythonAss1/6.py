
#Write a program to read string and print each character separately.     a) Slice the string using slice operator [:] slice the portion the strings to create a sub strings.     b) Repeat the string 100 times using repeat operator *     c) Read string 2 and concatenate with other string using + operator

myStr = "Hello Python"
for char in myStr:
    print(char)
print("\nSet of sub-string myStr[2:5] is: " ,  myStr[2:5])

repeatStr = myStr*100
print("\nThe repeat string is: ",repeatStr)
inputStr = input("\n\nEnter your string: ")
print("the concatenated string is")
print(myStr + inputStr)
