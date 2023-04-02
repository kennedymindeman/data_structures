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
        for item in [] if iterable is None else iterable:
            self.insert(SinglyLinkedList.Node(item))

    def insert(self, node: SinglyLinkedList.Node) -> None:
        """Inserts a new node into the linked list

        :param node: The node to insert
        :raises InvalidListEndExcpetion: insert is called on a list
        with an invalid end node
        """
        if self.head is None:
            self.head = node
            self.end = node
            return

        if self.end is None:
            raise InvalidListEndExcpetion

        self.end.next_node = node
        self.end = node

    def __iter__(self):
        self.curr = self.head
        return self

    def __next__(self):
        if self.curr is None:
            raise StopIteration

        val = self.curr.val
        self.curr = self.curr.next_node
        return val
