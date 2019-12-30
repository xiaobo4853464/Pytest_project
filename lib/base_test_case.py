import inspect
import os
from functools import wraps

from lib.Json_handler import json_get, jsonFile_get


class BaseTestCase(object):
    def assert_equal(self, expect, actual, msg):
        assert expect == actual, msg

    def get_testdata2(self):
        test_data_path = inspect.getfile(self.__class__).replace("cases", "testdata").replace(".py", ".json")

        expr_with_testcase = "$..%s" % self.testcase_name.lower()
        testdata = jsonFile_get(test_data_path, expr_with_testcase)

        return testdata



def get_testdata_dec(input_values=False):
    def get_testdata_decorator(func):
        @wraps(func)
        def wrapped(*args,**kwargs):
            all_testdata = get_testdata(args[0])
            jsonpath_for_expected = "$..expected_values"
            expect_data = json_get(all_testdata, jsonpath_for_expected) or all_testdata
            testdata = expect_data
            if input_values:
                jsonpath_for_input = "$..input_values"
                input_data = json_get(all_testdata, jsonpath_for_input)
                testdata = (expect_data, input_data)

            args[0].testdata = testdata
            return func(*args,**kwargs)

        return wrapped

    return get_testdata_decorator


def get_input_data(self):
    all_testdata = self.get_testdata()
    jsonpath_for_input = "$..input_values"
    return json_get(all_testdata, jsonpath_for_input) or all_testdata


def get_testdata(obj):
    test_data_path = inspect.getfile(obj.__class__).replace("cases", "testdata").replace(".py", ".json")

    expr_with_testcase = "$..%s" % obj.testcase_name.lower()
    testdata = jsonFile_get(test_data_path, expr_with_testcase)

    # current_branch = "4.5.300"  # sample
    # if current_branch:
    #     current_branch = 'branch_' + current_branch.replace('.', '_')
    #     branch_group = current_branch[0:10] + '_all'
    # else:
    #     current_branch = " "
    #     branch_group = " "
    # priority_list = [current_branch, branch_group, "common"]
    # testdata_with_branch = json_get_with_priority(testdata, priority_list) or testdata
    #
    # # with platform
    # platform = "windows"  # sample
    # expr_with_platform = "$..%s" % platform
    # testdata_with_platform = json_get(testdata_with_branch, expr_with_platform) or testdata_with_branch

    return testdata

def get_testdata2(obj):
    test_data_path = inspect.getfile(obj.__class__).replace("cases", "testdata").replace(".py", ".json")

    expr_with_testcase = "$..%s" % obj.testcase_name.lower()
    testdata = jsonFile_get(test_data_path, expr_with_testcase)

    return testdata