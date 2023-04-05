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
        pass
