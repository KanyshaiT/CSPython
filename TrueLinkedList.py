class Node(object):
    def __init__(self, d):
        self.next_node= None
        self.data= d

class LinkedList(object):
    def __init__(self):
        self.head= None
        self.tail= None
        self.size = 0

    def add(self, d):
        new_node = Node(d)
        if self.tail:
            self.tail.next_node = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        self.size += 1

    def add_at(self, d, index):
        new_node = Node(d)
        previous_node = None
        current_node = self.head
        i = 0
        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1
        if i == index:
            previous_node.next_node = new_node
            new_node.next_node = current_node
            return True
        else:
            #List is not long enough
            return False

    def remove(self, d):
        previous_node = None
        current_node = self.head
        while current_node:
            if current_node.data == d:
                if previous_node:
                    previous_node.next_node = current_node.next_node
                else:
                    self.head = current_node.next_node
                self.size -= 1
                return True
            previous_node = current_node
            current_node = current_node.next_node
        return False

    def remove_at(self, index):
        '''
        This function removes the node at a given index
        >>>a.to_list()
        [1,2,3]
        >>>a.remove_at(0)
        >>>a.to_list()
        [2,3]
        :param index: Index of an element in LinkedList which you want to delete
        :return: Return True if the element was successfully removed
        '''

        previous_node = None
        current_node = self.head
        i = 0
        while i < index and current_node.next_node:
            previous_node = current_node
            current_node = current_node.next_node
            i += 1
        if i == index:
            if previous_node:
                previous_node.next_node = current_node.next_node
            else:
                self.head = current_node.next_node
            self.size -= 1
            return True
        previous_node = current_node
        current_node = current_node.next_node

    def find(self, d):
        current_node = current_head
        while current_node:
            if current_node.data == d:
                return True
            current_node = current_node.next_node
        return False

    def find_at(self, index):
        current_node = self.head
        i = 0
        while i < index and current_node.next_node:
            current_node = current_node.next_node
            i += 1
        if i==index:
            return current_node.data



    def to_list(self):
        l = []
        current_node = self.head
        while current_node:
            l.append(current_node.data)
            current_node = current_node.next_node
        return l



'''a= LinkedList()
a.add(5)
a.add(6)
a.add(8)
print(a.to_list())
a.add_at(7, 2)
print(a.to_list())
print(a.remove(5))
print(a.remove(9))
a.remove_at(0)
print(a.to_list())
print(a.find_at(1))'''





