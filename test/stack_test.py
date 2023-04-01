"""Test suite for Stack class"""
from src.stack import Stack


def test_stack_constructor():
    """Tests the constructor of the Stack object"""
    assert isinstance(Stack(), Stack)
