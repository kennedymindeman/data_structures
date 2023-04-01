"""Stack class file"""


import copy
from typing import Iterable, Optional


class Stack:
    """Stack class that supports LIFO operations"""

    def __init__(self, iterable: Optional[Iterable] = None):
        self._list = list(iterable) if iterable else []

    def push(self, item: object) -> None:
        """Push an item onto the stack

        :param item: The item to add to the stack
        :return: True if adding the item was successful false otherwise
        """
        self._list.append(item)

    def peek(self):
        """Peeks at the top of the stack

        :return: A deep copy of the item on top of the stack
        """
        return copy.deepcopy(self._list[-1])
