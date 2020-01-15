import pytest


class TestSetupTeardown(object):
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
