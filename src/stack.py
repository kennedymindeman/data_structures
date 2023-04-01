"""Stack class file"""


from typing import Iterable, Optional


class Stack:
    """Stack class that supports LIFO operations"""

    def __init__(self, iterable: Optional[Iterable] = None):
        self._list = list(iterable) if iterable else []

    def push(self, item: object) -> bool:
        """Push an item onto the stack

        :param item: The item to add to the stack
        :return: True if adding the item was successful false otherwise
        """
        try:
            self._list.append(item)
            return True
        except MemoryError:
            return False
