from data_structures.invalid_operation_error import InvalidOperationError

"""
    A Queue class implementing a first-in, first-out (FIFO)
    data structure using a Linked List as the underlying storage mechanism.
"""

    # class InvalidOperationError(Exception):


class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node


class Queue:

    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        value = self.front.value
        self.front = self.front.next_node
        if self.front is None:
            self.rear = None
        return value  # This line should be outside the conditional block.


    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None


