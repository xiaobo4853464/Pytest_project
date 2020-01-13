import unittest

import pytest

from lib.base_test_case import BaseTestCase


class TestGetTestData(BaseTestCase):
    @pytest.fixture(scope="class", autouse=True)
    def fixx(self):
        self.__class__.a = 1

    def test_case1(self, test_case1):
        self.assert_equal(1,1)
        # print(os.path.abspath(os.path.dirname(__file__)))
        print(self.a)
        print(test_case1)

    def test_case2(self, test_case2):
        # self.assert_equal(1,2,"this is error")
        self.assert_equal(1,1,"this is error")

    # def test_case3(self):
    #     self.assert_equal(1,2)


class TestDemo(unittest.TestCase):
    def test_1(self):
        self.assertEqual(1,1)