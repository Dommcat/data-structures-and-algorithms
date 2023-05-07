
"""
Feature Tasks
Write the following methods for the Linked List class:

append
arguments: new value
adds a new node with the given value to the end of the list


insert before
arguments: value, new value
adds a new node with the given new value immediately before the first node that has the value specified


insert after
arguments: value, new value
adds a new node with the given new value immediately after the first node that has the value specified

"""

class Node: # node in a singly-linked list
    """
    A node in a singly-linked list.
    Attributes:
        value (any): The value stored in the node.
        next (Node): The next node in the list.
    """
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class LinkedList:
    """
    A singly-linked list.
    Attributes:
        head (Node): The first node in the linked list.
    """
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node

    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(f"{{ {current.value} }} ->")
            current = current.next
        result.append("NULL")
        return " ".join(result) #"{ a } -> { b } -> { c } -> NULL"

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False



class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def __str__(self):
        values = []
        current = self.head
        while current:
            values.append(str(current.value))
            current = current.next
        return " -> ".join(values)










# #the traverse list +  3 required methods

#     def traverse_list(self):
#         current = self.head
#         while current is not None:
#             current.value += 1
#             current = current._next
#         return "There's something in the way she moves me"


















