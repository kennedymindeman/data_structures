"""List implemented using linked nodes"""


from typing import Iterable, Optional


class LinkedList:
    """List implemented using linked nodes"""

    class Node:
        """A node in a linked list"""

        def __init__(self, val, next_node):
            self.val = val
            self.next = next_node

    def __init__(self, iterable: Optional[Iterable] = None):
        pass
