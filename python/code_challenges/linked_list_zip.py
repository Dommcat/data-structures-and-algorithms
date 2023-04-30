from linked_list.linked_list import LinkedList

# def zip_lists(a, b):
#     pass


def zip_lists(list1, list2):
    if list1.head is None and list2.head is None:
        return None
    elif list1.head is None:
        return list2
    elif list2.head is None:
        return list1

    result = LinkedList()

    node1 = list1.head
    node2 = list2.head

    while node1 or node2:
        if node1:
            result.append(node1.value)
            node1 = node1._next
        if node2:
            result.append(node2.value)
            node2 = node2._next

    while node1 is not None:
        result.append(node1.value)
        node1 = node1._next

    while node2 is not None:
        result.append(node2.value)
        node2 = node2._next
    return result





# Source cite: trouble shooting pytest import links with adpated code from author Tyler Huntly linked_list_zip to test known working source code with pytest

