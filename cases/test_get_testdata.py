import pytest

from lib.base_test_case import BaseTestCase, get_testdata_dec, get_testdata2


class TestGetTestData(BaseTestCase):
    # @pytest.fixture(autouse=True)
    # def set_up_fixture(self,request):
    #     self.testcase_name=request.function.__name__
    #     print("test start")
    #
    # @get_testdata_dec()
    # def test_case1(self):
    #     print(1)

    @pytest.fixture(autouse=True)
    def set_up_fixture(self, request):
        self.testcase_name = request.function.__name__
        self.testdata = self.get_testdata()

    def test_case1(self):
        print(self.testdata)

    def test_case2(self):
        print(self.testdata)
