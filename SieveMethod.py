
def create_linked_list(n):
    from TrueLinkedList import LinkedList
    from TrueLinkedList import Node

    """
    This function creates a Linked List from to to n'th number
    >>>create_linked_list(5)
    [2,3,4,5]
    :param n: last element of new created linked list
    :return:
    """
    a = LinkedList()
    if n >= 2:
        for i in range(2, n+1):
            a.add(i)
        return a.to_list()

def elim

print(create_linked_list(5))
