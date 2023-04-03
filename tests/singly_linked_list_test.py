"""Test suite for singly linked list"""
from pytest import fixture

from src.singly_linked_list import SinglyLinkedList


@fixture(name="populated_list")
def make_populated_list():
    """Generates a populated list and returns it"""
    return [1, 2, 3, [[]], (7 // 8)]


def test_constructor():
    """Tests the constructor of a linked list"""
    assert isinstance(SinglyLinkedList(), SinglyLinkedList)


def test_iterable_constructor():
    """Tests the linked lists constructor when passed an iterable"""
    assert isinstance(SinglyLinkedList([1, 2, 3]), SinglyLinkedList)


def test_iteration():
    """Tests iteration over singly linked list"""
    lst = [1, 2, 3, [[]], (7 // 8)]
    assert list(SinglyLinkedList(lst)) == lst


def test_length():
    """Tests length method of singly linked list"""
    lst = [1, 2, 3, [[]], (7 // 8)]
    linked_list = SinglyLinkedList(lst)
    assert len(linked_list) == len(lst)


def test_item_at():
    """Tests item_at method of singly linked list"""
    lst = [1, 2, 3, [[]], (7 // 8)]
    linked_list = SinglyLinkedList(lst)
    for index, item in enumerate(lst):
        assert linked_list.item_at(index) == item


def test_remove(populated_list):
    """Tests remove method of singly linked list"""
    linked_list = SinglyLinkedList(populated_list)
    assert linked_list.remove(3) == populated_list[3]
    del populated_list[3]
    assert list(linked_list) == populated_list
    assert linked_list.remove(len(linked_list) - 1) == populated_list[-1]
