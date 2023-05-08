from stack_queue_brackets.invalid_op_error import InvalidOperationError

# class Stack:
#     def __init__(self):
#         self.items = []

#     def push(self, value):
#         self.items.append(value)

#     def pop(self):
#         return self.items.pop()

#     def peek(self):
#         return self.items[-1]

#     def is_empty(self):
#         return len(self.items) == 0




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
