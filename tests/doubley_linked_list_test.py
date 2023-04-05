"""Tests for doubly linked list class"""
from src.doubly_linked_list import DoublyLinkedList


def test_doubly_linked_list_constructor():
    """Tests the constructor of a linked list"""
    assert isinstance(DoublyLinkedList(), DoublyLinkedList)
