from data_structures.invalid_operation_error import InvalidOperationError

#Import invalid operation error
#pop & peek invoke the invalid operation error with the correct message
#relative imports and absolute syntax (what)

"""
A Stack class implementing a last-in, first-out (LIFO) data structure using a LL as the underlying storage mechanism.

    Attributes
    ----------
          : Node
        The top node of the stack.

    Methods
    -------
"""

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
















    #
    # def __init__(self):
    #     # initialization here
    #     pass
    #
    # def some_method(self):
    #     # method body here
    #     pass
