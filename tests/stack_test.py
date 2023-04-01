"""Test suite for Stack class"""
from pytest import fixture, raises

from src.stack import PoppedEmptyStackException, Stack


@fixture(name="populated_stack")
def make_populated_stack():
    """Sets up a stack with multiple elements on it

    :return: _description_
    """
    return Stack([1, 2, 3, [], 3.14])


def test_stack_constructor():
    """Tests the constructor of the Stack object"""
    assert isinstance(Stack(), Stack)


def test_stack_constructor_iterable(populated_stack):
    """Tests the constructor of the stack object when passed an
    iterable"""
    assert isinstance(populated_stack, Stack)


def test_push_on_empty_stack():
    """Tests the stack's push method"""
    stack = Stack()
    stack.push(1)


def test_push_on_non_empty_stack():
    """Tests results of pushing onto a stack that has an item on it"""
    stack = Stack([1])
    assert stack.peek() == 1
    assert stack.peek() != 2
    stack.push(2)
    assert stack.peek() == 2
    assert stack.peek() != 1
    lst = []
    stack.push(lst)
    assert stack.peek() == []
    assert stack.peek() is not lst


def test_pop_on_empty_stack():
    """Tests popping an empty stack"""
    with raises(PoppedEmptyStackException):
        Stack().pop()
