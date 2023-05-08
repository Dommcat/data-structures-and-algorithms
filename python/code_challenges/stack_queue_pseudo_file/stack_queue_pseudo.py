
"""
    A class representing a queue data structure implemented using two stacks.

    Attributes:
    ----------
    in_stack : list
        A list representing the input stack of the queue.
    out_stack : list
        A list representing the output stack of the queue.

    Methods:
    -------
    enqueue(value)
        Adds an element to the end of the queue.
    dequeue()
        Removes and returns the first element of the queue.
        """

class PseudoQueue:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, value):
        self.stack1.push(value)

    def dequeue(self):
        if self.stack1.is_empty() and self.stack2.is_empty():
            raise Exception('Queue is empty')
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        return self.stack2.pop()


# class Queue:
#     def __init__(self):
#         self.in_stack = []
#         self.out_stack = []

#     def enqueue(self, value):
#         self.in_stack.append(value)

#     def dequeue(self):
#         if not self.out_stack:
#             if not self.in_stack:
#                 raise IndexError("Cannot dequeue from an empty queue")
#             while self.in_stack:
#                 self.out_stack.append(self.in_stack.pop())
#         return self.out_stack.pop()



class Node:

    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Stack:
    def __init__(self):
        self.top = None

    def push(self, value):
        """Adds a new node with the specified value to the top of the stack."""
        new_node = Node(value, self.top)
        self.top = new_node

    def pop(self):
        """ Removes and returns the value of the node from the top of the stack.
            Raises an exception if the stack is empty."""
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        value = self.top.value
        self.top = self.top.next_node
        return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Method not allowed on empty collection")
        return self.top.value

    def is_empty(self):
        return self.top is None



