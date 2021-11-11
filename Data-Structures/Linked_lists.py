LINKED LISTS

                      1.1 Theory

A linked list is a sequential structure that consists of a sequence
of items in linear order which are linked to each other. Hence
you have access data sequentially and random access is not possible.
Linked lists provide a simple and flexible representation of dynamic sets.

                      1.2 Linked List Elements
  - Elements in a linked list are known as NODEs
  - Each node contains a KEY and a POINTER to its
                   successor node, known as NEXT
  - The attribute named HEAD points to the first
                   element of the linked list.
  - The last element of the linked list is known
                                   as the TAIL.


1.3 Linked List Image

  https://miro.medium.com/max/630/1*4fuF6lHXOSmoVNcOV8aaJA.png


1.4 Types Of Linked List

1 - SINGLY LINKED LIST --> Traversal of items can
      be done in the forward direction only.

2 - DOUBLY LINKED LIST --> Traversal of items can
      be done in both forward and backward directions.
      Nodes consist of an additional pointer known as PREV,
      pointing to the previous node

3 - CIRCULAR LINKED LIST --> Linked lists where the
        PREV pointer of the head points to the tail and
        the NEXT pointer of the tail points to the head


1.5 Application Of Linked Lists

- Used for symbol table management in compiler design

Code

1) Singly Linked List

class Box:
    def __init__(self, data):
        self.data = data
        self.ref = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_all(self):
        if self.head is None:
            print("Linked list is empty")
        else:
            container = self.head
            while container is not None:
                print(container.data)
                container = container.ref

    def add_begin(self, data):
        new_box = Box(data)
        new_box.ref = self.head
        self.head = new_box

    def add_end(self, data):
        new_node = Box(data)
        while self.head.ref is not None:
            self.head = self.head.ref
        self.head.ref = new_node

    def add_after(self, data, x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("Node is not present is LL")
        else:
            new_node = Box(data)
            new_node.ref = n.ref
            n.ref = new_node

    def add_before(self, data, x):
        if self.head is None:
            print("Empty")
            return

        if self.head.data == x:
            new_node = Box(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head

        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("Not found")
        else:
            new_node = Box(data)
            new_node.ref = n.ref
            n.ref = new_node

    def remove_begin(self):
        if self.head is not None:
            self.head = self.head.ref
            return

    def remove_end(self):
        if self.head is not None:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None


n = LinkedList()
n.add_begin(323)
n.add_end(55)
n.add_before(22, 55)
n.add_after(234, 323)
n.remove_end()
n.remove_begin()
n.print_all()
