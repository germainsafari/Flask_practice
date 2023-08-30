#filter() = creates a collection of elements from an iterable for which a fuction returns true

class Node:
    def __init__(self, data):
        self.data = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_LL(self):
        if self.head == None:
            print("no data")
        else:
            n = self.head
            while n is not None:
                print(n.data)
                n = n.ref
    def add_beginning(self, data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node


LL1 = LinkedList()
LL1.add_beginning(10)
LL1.add_beginning(20)
LL1.add_beginning(40)
LL1.print_LL()