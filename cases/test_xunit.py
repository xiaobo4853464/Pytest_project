import pytest


def setup_module(module):
    """ setup any state specific to the execution of the given module."""
    pass


def teardown_module(module):
    """ teardown any state that was previously setup with a setup_method call."""
    pass


def setup_function(function):
    """ setup any state tied to the execution of the given function.
        Invoked for every test function in the module.
    """
    pass


def teardown_function(function):
    """ teardown any state that was previously setup with a setup_function call."""
    pass


class TestXunit(object):
    @classmethod
    def setup_class(cls):
        cls.a = 1
        print("class setup")

    @classmethod
    def teardown_class(cls):
        print("class teardown")

    def test_1(self):
        print(self.a)
        print("test case 1")

    def test_2(self):
        print(self.a)
        print("test case 2")

    def setup_method(self, method):
        print("setup_method")

    def teardown_method(self, method):
        print("teardown_method")
