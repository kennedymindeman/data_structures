"""Stack class file"""


from copy import deepcopy
from typing import Iterable, Optional


class StackException(Exception):
    """Exception relating to a stack"""


class PoppedEmptyStackException(StackException):
    """An empty stack was popped"""


class Stack:
    """Stack class that supports LIFO operations"""

    def __init__(self, iterable: Optional[Iterable] = None):
        self._list = [] if iterable is None else list(iterable)

    def push(self, item: object) -> None:
        """Push an item onto the stack

        :param item: The item to add to the stack
        :return: True if adding the item was successful false otherwise
        """
        self._list.append(deepcopy(item))

    def peek(self) -> object:
        """Peeks at the top of the stack

        :return: A deep copy of the item on top of the stack
        """
        return deepcopy(self._list[-1])

    def pop(self) -> object:
        """Pops the item on top of the stack

        :return: The item on top of the stack
        """
        if len(self._list) <= 0:
            raise PoppedEmptyStackException("pop called on empty Stack")

        return self._list.pop()
