class LinkedList:

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



   def insert_before(self, value, new_value):
        if not self.head:
            raise ValueError("List is empty")

        if self.head.value == value:
            new_node = Node(new_value, self.head)
            self.head = new_node
            return

        current = self.head
        while current.next and current.next.value != value:
            current = current.next

        if not current.next:
            raise ValueError(f"Value {value} not found in the list")

        new_node = Node(new_value, current.next)
        current.next = new_node

    def insert_after(self, value, new_value):
        if not self.head:
            raise ValueError("List is empty")

        current = self.head
        while current and current.value != value:
            current = current.next

        if not current:
            raise ValueError(f"Value {value} not found in the list")

        new_node = Node

        class LinkedList:
            def __init__(self):
                self.head = None

            def kthFromEnd(self, k):
                if self.head is None:
                    raise Exception("The linked list is empty.")

                # Initialize two pointers, one pointing to the head and the other k nodes ahead.
                first = self.head
                second = self.head
                for i in range(k):
                    if second is None:
                        raise Exception("k is larger than the length of the linked list.")
                    second = second.next

                # Move both pointers until the second pointer reaches the end of the linked list.
                while second is not None:
                    first = first.next
                    second = second.next

                # At this point, the first pointer is k nodes from the end.
                return first.value

        #
        # LinkedList.insert(3)  # Adds a new node with the value 3 to the head of the list
        # LinkedList.insert(2)  # Adds a new node with the value 2 to the head of the list
        # LinkedList.insert(1)  # Adds a new node with the value 1 to the head of the list























