"""List implemented using linked nodes"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable, Optional


class SinglyLinkedListException(Exception):
    """Exception relating to singly linked list"""


class InvalidListEndExcpetion(SinglyLinkedListException):
    """The end of a singly linked list doesn't contain valid data"""


@dataclass
class SinglyLinkedList:
    """List implemented using linked nodes"""

    @dataclass
    class Node:
        """A node in a linked list"""

        def __init__(
            self,
            val: object,
            next_node: Optional[SinglyLinkedList.Node] = None,
        ) -> None:
            self.val = val
            self.next_node = next_node

    def __init__(self, iterable: Optional[Iterable] = None) -> None:
        self.head = None
        self.end = None
        self.curr = None
        self._length = 0
        for item in [] if iterable is None else list(iterable)[::-1]:
            self.insert(item)

    def insert(self, val: object, index: int = 0) -> None:
        """Inserts a new node into the linked list

        :param node: The node to insert
        :raises InvalidListEndExcpetion: insert is called on a list
        with an invalid end node
        """
        if index > len(self):
            raise IndexError

        self._length += 1
        curr = self.head
        for _ in range(index):
            curr = curr.next_node  # type: ignore

        self.head = SinglyLinkedList.Node(val, curr)  # type: ignore

    def item_at(self, index: int) -> object:
        """Finds the item at a given index

        :param index: index to who's value to find
        :return: item at index
        """
        if index > len(self):
            raise IndexError

        curr = self.head
        for _ in range(index):
            curr = curr.next_node  # type: ignore

        return curr.val  # type: ignore

    def remove(self, index: int) -> object:
        """Removes an object at an index from the list if it's present

        :param index: Index of item to remove
        :return: The object that was removed
        """
        if index >= len(self):
            raise IndexError

        curr = self.head
        prev = self.head
        for _ in range(index):
            prev = curr
            curr = curr.next_node  # type: ignore

        self._length -= 1
        return_val = curr.val  # type: ignore
        if curr is self.end:  # type: ignore
            self.end = prev
            prev.next_node = None  # type: ignore
            return return_val

        prev.next_node = curr.next_node  # type: ignore
        return return_val

    def __len__(self) -> int:
        return self._length

    def __iter__(self) -> SinglyLinkedList:
        self.curr = self.head
        return self

    def __next__(self) -> object:
        if self.curr is None:
            raise StopIteration

        val = self.curr.val
        self.curr = self.curr.next_node
        return val

    def __getitem__(self, index: int) -> object:
        return self.item_at(index)

    def __delitem__(self, index: int) -> None:
        self.remove(index)

    def __setitem__(self, index: int, value: object) -> None:
        self.remove(index)
        self.insert(SinglyLinkedList.Node(value))
