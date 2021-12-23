from lib.base_test_case import BaseTestCase


class TestGetTestData(BaseTestCase):

    def test_case1(self, data):
        print(type(data.a), data.a)

    def test_fixture_get_data_from_data_driven(self, data, get_data_from_json):
        print(data)
