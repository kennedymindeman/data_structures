"""Test suite for Stack class"""
from src.stack import Stack


def test_stack_constructor():
    """Tests the constructor of the Stack object"""
    assert isinstance(Stack(), Stack)


def test_stack_constructor_iterable():
    """Tests the constructor of the stack object when passed an
    iterable"""
    assert isinstance(Stack([1, 2, 3]), Stack)


def test_push_on_empty_stack():
    """Tests the stack's push method"""
    stack = Stack()
    assert stack.push(1)
