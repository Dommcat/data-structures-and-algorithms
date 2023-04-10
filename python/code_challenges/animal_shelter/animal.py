
"""
Challenge Type: Code Challenge / Algorithm

Feature Tasks
Create a class called AnimalShelter which holds only dogs and cats.
The shelter operates using a first-in, first-out approach.

Implement the following methods:

enqueue
Arguments: animal

animal can be either a dog or a cat object.
It must have a species property that is either "cat" or "dog"
It must have a name property that is a string.
dequeue

Arguments: pref

pref can be either "dog" or "cat"
Return: either a dog or a cat, based on preference.
If pref is not "dog" or "cat" then return null.
"""


class AnimalShelter:
    def __init__(self):
        self.dog_queue = Queue()
        self.cat_queue = Queue()

    def enqueue(self, animal):
        if animal.species == 'dog':
            self.dog_queue.enqueue(animal)
        elif animal.species == 'cat':
            self.cat_queue.enqueue(animal)
        else:
            raise ValueError("The animal must be either a dog or a cat.")

    def dequeue(self, pref):
        if pref == 'dog':
            if self.dog_queue:
                return self.dog_queue.pop(0)
            else:
                return None
        elif pref == 'cat':
            if self.cat_queue:
                return self.cat_queue.pop(0)
            else:
                return None
        else:
            return None



# Methods, enqueue, dequeue

class Animal:
    def __init__(self, species, name):
        self.species = species
        self.name = name



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
            return value

    def peek(self):
        if self.is_empty():
            raise InvalidOperationError("Queue is empty")
        return self.front.value

    def is_empty(self):
        return self.front is None





if __name__=='__main__':

    dog1 = Animal("dog", "dog1")
    cat1 = Animal("cat", "cat1")
    cat2 = Animal("cat", "cat2")
    cat3 = Animal("cat", "cat3")

    shelter = AnimalShelter()

    # Enqueue

    shelter.enqueue(dog1)
    shelter.enqueue(cat1)
    shelter.enqueue(cat2)

    print(shelter.dog_queue.front.value)
