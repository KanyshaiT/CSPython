#Question 5
def f(x,y):
    if x>0:
        f(x-1, y)
    elif y>0:
        f(x, y-1)
    print(x)
    print(y)

'''
>>>print (f(3,3))
0
0
0
1
0
2
0
3
1
3
2
3
3
3
'''

#question 3
import LinkedList
def elim_second_odd(l):
    if l.head == None:
        return "Your list Linked LIst is empty!"
    else:

