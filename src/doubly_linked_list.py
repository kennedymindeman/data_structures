"""Doubly linked list implementation"""
from __future__ import annotations

from typing import Iterable, Optional


class DoublyLinkedList:
    """A linked list with nodes able to access the nodes before and after them"""

    class Node:
        """A node in a doubly linked list"""

        def __init__(
            self,
            val: object,
            prev_node: Optional[DoublyLinkedList.Node] = None,
            next_node: Optional[DoublyLinkedList.Node] = None,
        ) -> None:
            self.val = val
            self.prev_node = prev_node
            self.next_node = next_node

    def __init__(self, iterable: Optional[Iterable] = None) -> None:
        self.head = None
        self.tail = None
        self._length = 0
        for item in iterable or []:
            self.insert(item)

    def insert(self, val: object, index=0) -> None:
        """Inserts an item into the list at a specifed position

        :param val: The value to insert into the list
        :param index: The index at which to insert the item, defaults to 0
        """
        self._length += 1
        if index > self._length or self.head is None:
            raise IndexError

        curr = self.head
        for _ in range(index):
            curr = curr.next_node
            if curr is None:
                raise IndexError

        prev_node = None if curr is None else curr.prev_node
        new_node = DoublyLinkedList.Node(val, prev_node, curr)
        curr.prev_node = new_node
        if prev_node is not None:
            prev_node.next_node = new_node

        if new_node.next_node is None:
            self.tail = new_node

        if new_node.prev_node is None:
            self.head = new_node
