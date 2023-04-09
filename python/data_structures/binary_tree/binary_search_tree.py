from data_structures.binary_tree.trees import BinaryTree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree(BinaryTree):
    """
Create a Binary Search Tree class: This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
Add:
Arguments: value
Return: nothing
Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
    """
    def __init__(self):
        self.root = None

    def add (self, value):
        # method body here
        node = Node(value)
        if not self.root:
            self.root = node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = node
                        break
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = node
                        break
                    else:
                        current = current.right
        return


    def contains(self, value):
        if not self.root:
            return False
        else:
            current = self.root
            while current:
                if value == current.value:
                    return True
                elif value < current.value:
                    current = current.left
                else:
                    current = current.right
            return False








#     def contains(self):
#         pass




