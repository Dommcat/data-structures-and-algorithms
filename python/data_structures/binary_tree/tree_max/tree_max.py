class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self, root=None):
        self.root = root
        self.left = None
        self.right = None


 def find_maximum_value(self):
        if not self.root:
            return float('-inf')
        max_val = self.root.value
        #max_value is = 10
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node.value > max_val:
                max_val = node.value
            if node.left:
                stack.append(node.left)
                # mode.left =30
            if node.right:
                stack.append(node.right)
                # = -7
        return max_val






    # def find_maximum_value(self):
    #     if not self.root:
    #         return float('-inf')
    #     max_val = Node.value
    #     left_max = self.find_maximum_value(Node.left)
    #     right_max = self.find_maximum_value(Node.right)
    #     if left_max > max_val:
    #         max_val = left_max
    #     if right_max > max_val:
    #         max_val = right_max
    #     return max_val

    # def find_maximum_value(self,value=0):
    #     if not self.root:
    #         return float('-inf')
    #     max_val = self.root
    #     left_max = self.find_maximum_value(self.left)
    #     right_max = self.find_maximum_value(self.right)
    #     if left_max > max_val:
    #         max_val = left_max
    #     if right_max > max_val:
    #         max_val = right_max
    #     return max_val

    # def find_maximum_value(self):
    #     if not self.root:
    #         return float('-inf')
    #     max_val = self.root.value
    #     left_max = self.left.find_maximum_value() if self.left else float('-inf')
    #     right_max = self.right.find_maximum_value() if self.right else float('-inf')
    #     if left_max > max_val:
    #         max_val = left_max
    #     if right_max > max_val:
    #         max_val = right_max
    #     return max_val







# def find_maximum_value(self): - This is the function signature that defines the find_maximum_value method as a member of the BinaryTree class.

# if not self.root: - This line checks if the root node of the binary tree is None or not. If the root is None, it means that the tree is empty, and the function returns negative infinity.

# max_val = self.root.value - This line initializes the maximum value found so far to be the value of the root node of the binary tree.

# stack = [self.root] - This line initializes a stack with the root node of the binary tree as the only element.

# while stack: - This line starts a loop that continues until the stack is empty.

# node = stack.pop() - This line pops the last element from the stack and assigns it to the node variable. This is equivalent to performing a depth-first traversal of the binary tree.

# if node.value > max_val: - This line checks if the value of the current node is greater than the current maximum value found so far. If it is, the maximum value is updated to be the value of the current node.

# if node.left: - This line checks if the current node has a left child node. If it does, the left child node is added to the stack.

# if node.right: - This line checks if the current node has a right child node. If it does, the right child node is added to the stack.

# return max_val - This line returns the maximum value found in the binary tree.

#Sources: ChatGPT, random webs














