"""Test suite for singly linked list"""
from src.linked_list import LinkedList


def test_constructor():
    """Tests the constructor of a linked list"""
    assert isinstance(LinkedList(), LinkedList)


def test_iterable_constructor():
    """Tests the linked lists constructor when passed an iterable"""
    assert isinstance(LinkedList([1, 2, 3]), LinkedList)
