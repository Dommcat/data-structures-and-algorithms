

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


        """
        Insert a new node with the given value at the beginning of the list.
        """
    def insert(self, value):
        new_node = Node(value, self.head)
        self.head = new_node


        """
        Return a string representation of the list.
        """
    def __str__(self):
        result = []
        current = self.head
        while current:
            result.append(f"{{ {current.value} }} ->")
            current = current.next
        result.append("NULL")
        return " ".join(result) #"{ a } -> { b } -> { c } -> NULL"

# 3 methods

    """
      Check if the list contains a node with the given value.
    """

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    """
    Append a new node with the given value to the end of the list.
    """

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

        """
        Insert a new node with the given new value immediately before the first node that has the value specified.

        """

    def insert_before(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return
        if self.head.value == value:
            new_node.next = self.head
            self.head = new_node
            return
        current = self.head
        while current.next:
            if current.next.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Value not found: {value}") #        Raises a ValueError if the specified value is not found in the list.


    """
    Insert a new node with the given new value immediately after the first node that has the value specified.

    """


    def insert_after(self, value, new_value):
        new_node = Node(new_value)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current:
            if current.value == value:
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
        raise ValueError(f"Value not found: {value}") # Raises a ValueError if the specified value is not found in the list.














