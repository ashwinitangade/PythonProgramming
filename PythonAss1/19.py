#Using loop structures print even numbers between 1 to 100.   a) By using For loop, use continue/ break/ pass statement to skip odd numbers.     i) Break the loop if the value is 50     ii) Use continue for the values 10,20,30,40,50 b) By using while loop, use continue/ break/ pass statement to skip odd numbers.       i) Break the loop if the value is 90       ii) Use continue for the values 60,70,80,90

print("\nUsing for loop \nuse continue/ break/ pass statement to skip odd numbers.     \ni) Break the loop if the value is 50     \nii) Use continue for the values 10,20,30,40,50")
for num in range(0,100):
    if num%2==0:
        print(num)
        if num%10==0:
           if num==50:
              break;
           elif num<50:
              continue
           else:
              pass

print("\nBy using while loop, use continue/ break/ pass statement to skip odd numbers.       \ni) Break the loop if the value is 90       \nii) Use continue for the values 60,70,80,90")
num = 0
while num <=100:
    if num % 2 == 0:
        print(num)
        if num >= 60:
           if num % 10 == 0:
              if num == 90:
                 break
    else:
     pass
    num += 1
