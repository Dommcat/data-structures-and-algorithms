from data_structures.class_templates_file.class_temps import BinaryTree, Node

def breadth_first(tree_input):
    """
    Perform breadth-first search on a binary tree and return the node values in that order.

    :param tree_input: A binary tree.
    :type tree_input: Binary tree

    :return: A list of node values in breadth-first order.
    :rtype: list
    """

    # Initialize output_list
    output_list = [[],]

    if tree_input.root.value is None:
        return join_list(output_list)

    if tree_input.root.left is None and tree_input.root.right is None:
        output_list[0].append(tree_input.root.value)
        return join_list(output_list)

    def traverse(node, depth):
        """
        Recursively traverse the binary tree and add the node values to output_list.

        :param node: The current node of the binary tree.
        :type node: Binary tree node

        :param depth: The depth of the current node in the binary tree.
        :type depth: int

        :return: None
        """
        nonlocal output_list

        # initialize output_list
        if len(output_list) <= depth:
            output_list.append([])

        # Root
        output_list[depth].append(node.value)

        # Left
        if node.left:
            traverse(node.left, depth+1)

        # Right
        if node.right:
            traverse(node.right, depth+1)

    traverse(tree_input.root, 0)
    return join_list(output_list)

def join_list(list_input):
    """
    Join the sublists of a list of lists and return a flattened list.

    :param list_input: A list of lists.
    :type list_input: list

    :return: A flattened list of the sublists.
    :rtype: list
    """
    output_list = []
    for list_item in list_input:
        output_list += list_item
    return output_list
