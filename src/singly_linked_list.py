"""List implemented using linked nodes"""
from __future__ import annotations

from typing import Iterable, Optional


class SinglyLinkedListException(Exception):
    """Exception relating to singly linked list"""


class InvalidListEndExcpetion(SinglyLinkedListException):
    """The end of a singly linked list doesn't contain valid data"""


class SinglyLinkedList:
    """List implemented using linked nodes"""

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
        for item in [] if iterable is None else iterable:
            self.insert(SinglyLinkedList.Node(item))

    def insert(self, node: SinglyLinkedList.Node) -> None:
        """Inserts a new node into the linked list

        :param node: The node to insert
        :raises InvalidListEndExcpetion: insert is called on a list
        with an invalid end node
        """
        self._length += 1
        if self.head is None:
            self.head = node
            self.end = node
            return

        if self.end is None:
            raise InvalidListEndExcpetion

        self.end.next_node = node
        self.end = node

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
        for _ in range(index - 1):
            curr = curr.next_node  # type: ignore

        return_val = curr.next_node.val  # type: ignore
        curr.next_node = curr.next_node.next_node  # type: ignore
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
