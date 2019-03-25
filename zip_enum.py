#zip two lists into one
'''names= ["Jane", "Kate", "Johnny", "Depp"]
ages=[21,22,33,41]
combine = list(zip(names,ages))
>>>print (combine)
[('Jane', 21), ('Kate', 22), ('Johnny', 33), ('Depp', 41)]
'''

#unzip one list into two elements of one list

'''nameage=[('Jane', 21), ('Kate', 22), ('Johnny', 33), ('Depp', 41)]
unzip = list(zip(*nameage))
names = list(unzip[0])
age = list(unzip[1])
>>>print (names)
['Jane', 'Kate', 'Johnny', 'Depp']
>>>print(age)
[21, 22, 33, 41]
>>>print(unzip)
[('Jane', 'Kate', 'Johnny', 'Depp'), (21, 22, 33, 41)]
'''

#enum
names= ["Jane", "Kate", "Johnny", "Depp"]
'''for i in zip(range(len(names)), names):
    print(i)
    
    (0, 'Jane')
(1, 'Kate')
(2, 'Johnny')
(3, 'Depp')
'''
for i in enumerate(names):
    print(i)
'''
#gives the same result
(0, 'Jane')
(1, 'Kate')
(2, 'Johnny')
(3, 'Depp')
'''
