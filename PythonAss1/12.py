#Read 10 numbers from user and find the average of all. a) Use comparison operator to check how many numbers are less than average and print them b) Check how many numbers are more than average. c) How many are equal to average.

number_list = []
  
for i in range(0, 10):
    ele = int(input())
    number_list.append(ele) # adding the element

print('\nthe total elements added',len(number_list))
if len(number_list) > 0 and len(number_list) <= 10:
    print(number_list)
else:
    print('\nPlease enter 10 numbers')
    
sum_num = 0
avg = 0
for t in number_list:
    sum_num = sum_num + t

avg = sum_num / len(number_list)
print('\nAverage of entered numbers is : ',avg)
valueListMoreThanAvg = []
valueListLessThanAvg = []
valueListEqualToAvg = []
for element in number_list:
    if element > avg:
       valueListMoreThanAvg.append(element)
    elif element < avg:
        valueListLessThanAvg.append(element)
    elif element == avg:
       valueListEqualToAvg.append(element)
       
print('\nThe numbers which are more than average: ',valueListMoreThanAvg)
print('\nThe numbers which are less than average: ',valueListLessThanAvg)
print('\nThe numbers which are equal to average: ',valueListEqualToAvg)

