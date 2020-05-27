import unittest


class TestUnittest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print(cls)

    def test_1(self):
        print(self)


class A(object):
    @classmethod
    def haha(cls):
        print(cls)


A.haha()
