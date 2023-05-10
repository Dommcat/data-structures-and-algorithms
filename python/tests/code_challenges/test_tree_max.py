import pytest

from data_structures.class_templates_file.class_temps import BinaryTree, Node

from python.data_structures.binary_tree.tree_max.tree_max import BinaryTree, Node


# @pytest.mark.skip("TODO")
def test_max_val():
    tree = BinaryTree()
    tree.root = Node(10)
    tree.root.left = Node(30)
    tree.root.right = Node(-7)

    actual = tree.find_maximum_value()
    expected = 30

    assert actual == expected
