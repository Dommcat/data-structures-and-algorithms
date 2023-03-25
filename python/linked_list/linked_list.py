class LinkedList:
    """
   `Singly Linked List`. Singly Linked Lists contain individual nodes that have a reference to the

   The methods of this `LinkedList` are `insert`, `includes` and `str`.
    """

    def __init__(self, head, _next=None):
        self.head = None

    def __str__(self):  # same as to_string
        result = [str]
        current = self.head
        while current is not None:
            result.append(str(current))
            current = current._next
        return " -> ".join(result)

#the traverse list +  3 required methods

    def traverse_list(self):
        current = self.head
        while current is not None:
            current.value += 1
            current = current._next
        return "There's something in the way she moves me"

    def insert(self, head):
        self.head = head
        current = head
        while current is not None:
            current.value += 1
            current = current._next
        return "This is the insert method"

    def includes(self, head):
        current = self.head
        while current is not None:
            current.value += 1
            current = current._next
        return "This is the includes method"

   def to_string(self, head):
        current = self.head
        linked_list_string = ''
        while current is not None:
            current.value += 1
            current = current._next
        return linked_list_string + 'NULL'

class Node:  # node in a singly-linked list

            def __init__(self, head, next=None):
                self.head = head
                self._next = next

            def __str__(self):
                return f"Node({self.head}, {self.next})"








        #
        # LinkedList.insert(3)  # Adds a new node with the value 3 to the head of the list
        # LinkedList.insert(2)  # Adds a new node with the value 2 to the head of the list
        # LinkedList.insert(1)  # Adds a new node with the value 1 to the head of the list






















