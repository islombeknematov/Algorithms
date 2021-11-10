# LINKED LISTS

#                       1.1 Theory

# A linked list is a sequential structure that consists of a sequence
# of items in linear order which are linked to each other. Hence
# you have access data sequentially and random access is not possible.
# Linked lists provide a simple and flexible representation of dynamic sets.

#                       1.2 Linked List Elements
#   - Elements in a linked list are known as NODEs
#   - Each node contains a KEY and a POINTER to its
#                    successor node, known as NEXT
#   - The attribute named HEAD points to the first
#                    element of the linked list.
#   - The last element of the linked list is known
#                                    as the TAIL.


                        # 1.3 Linked List Image

#   https://miro.medium.com/max/630/1*4fuF6lHXOSmoVNcOV8aaJA.png


                        # 1.4 Types Of Linked List

# 1 - SINGLY LINKED LIST --> Traversal of items can
#       be done in the forward direction only.

# 2 - DOUBLY LINKED LIST --> Traversal of items can
#       be done in both forward and backward directions.
#       Nodes consist of an additional pointer known as PREV,
#       pointing to the previous node

# 3 - CIRCULAR LINKED LIST --> Linked lists where the
#         PREV pointer of the head points to the tail and
#         the NEXT pointer of the tail points to the head


                        # 1.5 Application Of Linked Lists

# - Used for symbol table management in compiler design

                        # Code

# 1) Singly Linked List

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        current = self.head

        while current.next != None:
            current = current.next
        current.next = new_node

    def length(self):
        concurrent = self.head
        total = 0
        while concurrent.next != None:
            total += 1
            concurrent = concurrent.next
        return total

    def display(self):
        elements = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node = cur_node.next
            elements.append(cur_node.data)
        print(elements)


my_list = LinkedList()

my_list.display()
my_list.append(2)
my_list.append(3)
my_list.display()



















