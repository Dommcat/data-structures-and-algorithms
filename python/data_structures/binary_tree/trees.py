


"""
Features
Binary Tree: Create a Binary Tree class
Define a method for each of the depth first traversals:
-pre order
-in order
-post order
Each depth first traversal method should return an array of values, ordered appropriately.

Binary Search Tree
Add:
Arguments: value
Return: nothing

Adds a new node with that value in the correct location in the binary search tree.
Contains
Argument: value
Returns: boolean indicating whether or not the value is in the tree at least once.
"""



class Node:
       # Node: Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.
    def  __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
        #Create a Binary Search Tree class: This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    def __init__(self, root=None):
        self.root = root

        #Traversal Method
    def pre_order(self, values =[]): # expected = ["a", "b", "d", "e", "c", "f", "g"]
              #root>>left>>right
        def walk(input_node, value_list):
            if not input_node:
                return
            # Do something with the root
            value_list.append(input_node.value)
            # Do something with root.left
            walk(input_node.left, value_list)
            # Do something with root.right1
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values


    def in_order(self, values =[]):# expected = ["d", "b", "e", "a", "f", "c", "g"]
            # left >> root >> right
        def walk(input_node, value_list):
            if not input_node:
                return
           # Do something with root.left
            walk(input_node.left, value_list)
            # Do something with the root
            value_list.append(input_node.value)
            # Do something with root.right
            walk(input_node.right, value_list)

        walk(self.root, values)
        return values


    def post_order(self, values = []):# expected = ["d", "e", "b", "f", "g", "c", "a"]
        # left >> right >> root
        def walk(input_node, value_list):
            if not input_node:
                return
            # Do something with root.left
            walk(input_node.left, value_list)
            # Do something with root.right
            walk(input_node.right, value_list)
            # Do something with the root
            value_list.append(input_node.value)

        walk(self.root, values)
        return values















