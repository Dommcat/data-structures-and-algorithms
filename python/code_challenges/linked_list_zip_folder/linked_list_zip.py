from linked_list.linked_list_template import  Node, LinkedList


def zip_lists(list1, list2):
    """
    Merge two linked lists by alternating nodes from each list.

    Args:
        list1 (LinkedList): The first linked list to merge.
        list2 (LinkedList): The second linked list to merge.

    Returns:
        LinkedList: A new linked list containing the merged nodes from both input lists.
    """
    # Handle the case where both input lists are empty.
    if list1.head is None and list2.head is None:
        return None

    # Handle the case where one input list is empty.
    elif list1.head is None:
        return list2
    elif list2.head is None:
        return list1

    # Create a new linked list to hold the merged nodes.
    result = LinkedList()

    # Iterate over both input lists and add nodes to the result list.
    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        # Add the next node from the first list to the result.
        if node1:
            result.append(node1.value)
            node1 = node1.next

        # Add the next node from the second list to the result.
        if node2:
            result.append(node2.value)
            node2 = node2.next

    # Append any remaining nodes from the first list to the result.
    while node1 is not None:
        result.append(node1.value)
        node1 = node1.next

    # Append any remaining nodes from the second list to the result.
    while node2 is not None:
        result.append(node2.value)
        node2 = node2.next

    # Return the merged linked list.
    return result



# Iterated TH code through Chatgpt to understand attribute error - relsolved and cleaned in final code block.
