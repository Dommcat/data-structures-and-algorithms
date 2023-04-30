from linked_list.linked_list import LinkedList

class Hashtable:
    """
    Implement a Hashtable Class with the following methods:set, get, has, keys, hash:
    """
    def __init__(self, size=1024):
        self._size = size
        self._buckets = size * [None]

    def hash(self, key):
        hash_total = 0
        for char in key:
            hash_total += ord(char)
        primed_number = hash_total * len(key) * 19
        index = primed_number % self._size
        return index


    def set(self, key, value):
        index = self.hash(key)
        if self._buckets[index] is None:
            self._buckets[index] = Node(key, value)
        else:
            self._buckets[index].add(key, value)


    def get(self, key):
        index = self.hash(key)
        if self._buckets[index] is None:
            return None
        else:
            return self._buckets[index].get(key)

    def has(self, key):
        index = self.hash(key)
        if self._buckets[index] is None:
            return False
        else:
            return True

    def keys(self):
        keys = []
        for item in self._buckets:
            if item:
                keys += [pair[0] for pair in item.display()]
        return keys


class Node:
    def __init__(self, key, value):
        self.data = [[key, value]]
        self.next = None

    def add(self, key, value):
        self.data.append([key, value])

    def remove(self, key):
        for pair in self.data:
            if pair[0] == key:
                self.data.remove(pair)
                break

    def get(self, key):
        for pair in self.data:
            if pair[0] == key:
                return pair[1]
        return None

    def display(self):
        return self.data







