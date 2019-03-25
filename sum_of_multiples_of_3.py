'''total=0
for i in range(1,9):
    if i%3 == 0:
        total +=i
print(total)
'''
#sum of multiples of 3 and 5 less that 100
'''total=0
for i in range(1,100):
    if i % 3 ==0 or i % 5 == 0:
        total +=i

print(total)'''


#typing once, twice ...

'''list=["hi", 'my', 'is', 'Stitch']
for i in range(len(list)):
    for j in range (i+1):
        print (list[i])
'''

#Sum of only the negative numbers in the list

list =[7,6,5,4,3,2,1,-1,-2,-3,-4,-5,-7]
sum=0
for i in list:
    if i <0:
        sum +=i
print(sum)
