"""Test suite for Stack class"""
from pytest import fixture, raises

from src.stack import (
    PoppedEmptyStackException,
    RanTopOnEmptyStackException,
    Stack,
)


@fixture(name="populated_stack")
def make_populated_stack():
    """Sets up a stack with multiple elements on it

    :return: _description_
    """
    return Stack([1, 2, 3, [], 3.14])


def test_stack_constructor():
    """Tests the constructor of the Stack object"""
    assert isinstance(Stack(), Stack)


def test_stack_constructor_iterable(populated_stack: Stack):
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
    assert stack.top() == 1
    assert stack.top() != 2
    stack.push(2)
    assert stack.top() == 2
    assert stack.top() != 1
    lst = []
    stack.push(lst)
    assert stack.top() == []
    assert stack.top() is not lst


def test_pop_on_empty_stack():
    """Tests popping an empty stack"""
    with raises(PoppedEmptyStackException):
        Stack().pop()


def test_empty():
    """Tets the empty method of the Stack class"""
    stack = Stack()
    assert stack.empty()
    stack.push(1)
    assert not stack.empty()
    stack.pop()
    assert stack.empty()


def test_top_on_empty_stack():
    """Tests behavior of top when called on an empty stack"""
    with raises(RanTopOnEmptyStackException):
        Stack().top()
