l1=[1,2,3,4,5,6,7,7]
l2=[4,5,6,7,8,9]
l3=[]

def common(l1,l2):
    """
    this function takes two lists as a parameter and finds common elements of them
    by creating a third list
    >>>common(l1,l2)
    [4,5,6]
    :param l1:
    :param l2:
    :return:
    """
    for i in l1:
        if i in l2 and i not in l3:
            l3.append(i)
    return l3
print(common(l1,l2))
