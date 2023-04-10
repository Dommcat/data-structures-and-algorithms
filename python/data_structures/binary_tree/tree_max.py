class BinaryTree:
      def __init__(self, root=None):
        self.root = root


class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def max_value(root: TreeNode) -> int:
    if not root:
        return float('-inf')
    max_val = root.val
    left_max = max_value(root.left)
    right_max = max_value(root.right)
    if left_max > max_val:
        max_val = left_max
    if right_max > max_val:
        max_val = right_max
    return max_val
