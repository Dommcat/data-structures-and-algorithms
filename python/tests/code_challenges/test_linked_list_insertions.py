import pytest
from data_structures.linked_list_insertions.insertions import LinkedList

def test_1_append():
    """
    Test 1: Test that a node can be appended to an empty linked list using the append() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    assert str(linked_list) == "{ apple } -> NULL"


def test_2_append_multiple():
    """
    Test 2: Test that multiple nodes can be appended to a linked list using the append() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.append("cherry")
    assert str(linked_list) == "{ apple } -> { banana } -> { cherry } -> NULL"


def test_3_insert_before_middle():
    """
    Test 3: Test that a node can be inserted before a node located in the middle of a linked list using the insert_before() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.append("cherry")
    linked_list.insert_before("banana", "apricot")
    assert str(linked_list) == "{ apple } -> { apricot } -> { banana } -> { cherry } -> NULL"


def test_4_insert_before_first():
    """
    Test 4: Test that a node can be inserted before the first node of a linked list using the insert_before() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.insert_before("apple", "apricot")
    assert str(linked_list) == "{ apricot } -> { apple } -> { banana } -> NULL"


def test_5_insert_after_middle():
    """
    Test 5: Test that a node can be inserted after a node located in the middle of a linked list using the insert_after() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.append("cherry")
    linked_list.insert_after("banana", "blueberry")
    assert str(linked_list) == "{ apple } -> { banana } -> { blueberry } -> { cherry } -> NULL"


def test_6_insert_after_last():
    """
    Test 6: Test that a node can be inserted after the last node of a linked list using the insert_after() method.
    """
    linked_list = LinkedList()
    linked_list.append("apple")
    linked_list.append("banana")
    linked_list.insert_after("banana", "cherry")
    assert str(linked_list) == "{ apple } -> { banana } -> { cherry } -> NULL"





# # @pytest.mark.skip("TODO")
# def test_append():
#     linked_list = LinkedList()

#     linked_list.insert("apple")

#     linked_list.insert("banana")

#     linked_list.append("cucumber")

#     assert str(linked_list) == "{ banana } -> { apple } -> { cucumber } -> NULL"


# # @pytest.mark.skip("TODO")
# def test_insert_before():
#     linked_list = LinkedList()

#     linked_list.insert("apple")

#     linked_list.insert("banana")

#     linked_list.insert_before("apple", "cucumber")

#     assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"


# # @pytest.mark.skip("TODO")
# def test_insert_before_first():
#     linked_list = LinkedList()

#     linked_list.insert("apple")

#     linked_list.insert_before("apple", "cucumber")

#     assert str(linked_list) == "{ cucumber } -> { apple } -> NULL"


# # @pytest.mark.skip("TODO")
# def test_insert_after():
#     linked_list = LinkedList()

#     linked_list.insert("apple")

#     linked_list.insert("banana")

#     linked_list.insert_after("banana", "cucumber")

#     assert str(linked_list) == "{ banana } -> { cucumber } -> { apple } -> NULL"



# @pytest.mark.skip("TODO")
# def test_insert_before_empty():
#     linked_list = LinkedList()

#     with pytest.raises(TargetError):
#         linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
# def test_insert_before_missing():
#     linked_list = LinkedList()

#     linked_list.insert("banana")

#     with pytest.raises(TargetError):
#         linked_list.insert_before("radish", "zucchinni")


# @pytest.mark.skip("TODO")
# def test_insert_after_empty():
#     linked_list = LinkedList()

#     with pytest.raises(TargetError):
#         linked_list.insert_after("radish", "zucchinni")


# @pytest.mark.skip("TODO")
# def test_insert_after_missing():
#     linked_list = LinkedList()

#     linked_list.insert("banana")

#     with pytest.raises(TargetError):
#         linked_list.insert_after("radish", "zucchinni")
