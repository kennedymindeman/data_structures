"""Stack class file"""


from typing import Iterable, Optional


class Stack:
    """Stack class that supports LIFO operations"""

    def __init__(self, iterable: Optional[Iterable] = None):
        self._list = list(iterable) if iterable else []
