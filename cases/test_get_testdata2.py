"""多个case 测试GDATA缓存是否ok"""
from lib.base_test_case import BaseTestCase


class TestGetTestData(BaseTestCase):

    def test_case1(self, data):
        print(type(data.a), data.a)
