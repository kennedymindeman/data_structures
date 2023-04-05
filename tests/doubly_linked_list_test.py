"""Tests for doubly linked list class"""
from src.doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list_constructor():
    """Tests the constructor of a linked list"""
    assert isinstance(DoublyLinkedList(), DoublyLinkedList)


def test_doublye_linked_list_constructor_with_iterable():
    """Tests the constructor of a linked list with an iterable"""
    assert isinstance(DoublyLinkedList([1, 2, 3]), DoublyLinkedList)
