"""Test suite for singly linked list"""
from src.singly_linked_list import SinglyLinkedList


def test_constructor():
    """Tests the constructor of a linked list"""
    assert isinstance(SinglyLinkedList(), SinglyLinkedList)


def test_iterable_constructor():
    """Tests the linked lists constructor when passed an iterable"""
    assert isinstance(SinglyLinkedList([1, 2, 3]), SinglyLinkedList)


def test_iteration():
    """Tests iteration over linked list"""
    lst = [1, 2, 3, [[]], (7 // 8)]
    assert list(SinglyLinkedList(lst)) == lst