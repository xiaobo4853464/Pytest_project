import inspect
import os
from functools import wraps

from lib.Json_handler import json_get, jsonFile_get


class BaseTestCase(object):
    def assert_equal(self, expect, actual, msg):
        assert expect == actual, msg

    def get_testdata(self):
        test_data_path = inspect.getfile(self.__class__).replace("cases", "testdata").replace(".py", ".json")

        expr_with_testcase = "$..%s" % self.testcase_name.lower()
        testdata = jsonFile_get(test_data_path, expr_with_testcase)

        return testdata


def get_testdata_dec(input_values=False):
    def get_testdata_decorator(func):
        @wraps(func)
        def wrapped(*args, **kwargs):
            all_testdata = get_testdata(args[0])
            jsonpath_for_expected = "$..expected_values"
            expect_data = json_get(all_testdata, jsonpath_for_expected) or all_testdata
            testdata = expect_data
            if input_values:
                jsonpath_for_input = "$..input_values"
                input_data = json_get(all_testdata, jsonpath_for_input)
                testdata = (expect_data, input_data)

            args[0].testdata = testdata
            return func(*args, **kwargs)

        return wrapped

    return get_testdata_decorator


def get_testdata(file_path, function_name):
    test_data_path = file_path.replace("cases", "testdata").replace(".py", ".json")

    expr_with_testcase = "$..%s" % function_name.lower()
    testdata = jsonFile_get(test_data_path, expr_with_testcase)

    return testdata
