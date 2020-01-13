import inspect
import os
from functools import wraps

from lib.Json_handler import json_get, jsonFile_get

import inspect


class BaseTestCase(object):
    # def print_test_message(self, expected_value, compared_diff_msg):
    #     '''
    #     print the checkpoints' test result as human language
    #     '''
    #     for check_point, expected in expected_value.items():
    #         try:
    #             checkpoint_detail_result = json_get(ast.literal_eval(str(compared_diff_msg).
    #                                                                  replace("[", "").
    #                                                                  replace("]", "").
    #                                                                  replace('"', "")), "$..%s" % check_point)
    #         except:
    #             checkpoint_detail_result = compared_diff_msg
    #         pass_the_checkpoint = checkpoint_detail_result is None
    #         print_message = check_point.replace("_", " ")
    #         if isinstance(expected, bool):
    #             if expected == False:
    #                 print_message = (print_message.replace("is", "is not")
    #                                  .replace("appear", "not appear")
    #                                  .replace("exist", "not exist"))
    #         if pass_the_checkpoint:
    #             if isinstance(expected, bool):
    #                 print("[pass check point] check %s" % print_message)
    #             else:
    #                 print("[pass check point] check %s with [expected_value]--> %s" % (print_message, expected))
    #         else:
    #             if isinstance(expected, bool):
    #                 checkpoint_detail_result = ""
    #             else:
    #                 checkpoint_detail_result = ("\r\n[compare result]:\r\n"
    #                                             + json.dumps(checkpoint_detail_result, indent=4, ensure_ascii=False))
    #             print("[fail check point] check %s" % (print_message + checkpoint_detail_result))

    _type_equality_funcs = {}

    def _set_up(self):
        self.addTypeEqualityFunc(dict, 'assertDictEqual')
        self.addTypeEqualityFunc(list, 'assertListEqual')
        self.addTypeEqualityFunc(tuple, 'assertTupleEqual')
        self.addTypeEqualityFunc(set, 'assertSetEqual')
        self.addTypeEqualityFunc(frozenset, 'assertSetEqual')
        self.addTypeEqualityFunc(str, 'assertMultiLineEqual')

    def addTypeEqualityFunc(self, typeobj, function):
        self._type_equality_funcs[typeobj] = function

    def _getAssertEqualityFunc(self, first, second):
        self._set_up()
        if type(first) is type(second):
            asserter = self._type_equality_funcs.get(type(first))
            if asserter is not None:
                if isinstance(asserter, str):
                    asserter = getattr(self, asserter)
                return asserter

        return self._baseAssertEqual

    def _baseAssertEqual(self, first, second, msg=None):
        """The default assertEqual implementation, not type specific."""
        if not first == second:
            raise AssertionError("%s != %s" % (first, second))
            # standardMsg = '%s != %s' % _common_shorten_repr(first, second)
            # msg = self._formatMessage(msg, standardMsg)
            # raise self.failureException(msg)

    def assert_equal(self, first, second, output_failed_msg=None,
                     checkpoint_description=None, **options):
        assertion_func = self._getAssertEqualityFunc(first, second)
        # assertion_func(first, second, msg=output_failed_msg)

        return self.assert_it(assertion_func, (first, second), output_failed_msg,
                              method_name=inspect.stack()[0][3], **options)

    # def assert_notequal(self, current_result, expected_result, output_success_msg=None, output_failed_msg=None,
    #                     checkpoint_description=None, stop_on_error=False, collect_report=True, **options):
    #     return self.assert_it(self.assertNotEqual, (current_result, expected_result), output_success_msg,
    #                           output_failed_msg, checkpoint_description=checkpoint_description,
    #                           method_name=inspect.stack()[0][3], **options)
    #
    # def assert_true(self, current_result, output_success_msg=None, output_failed_msg=None, checkpoint_description=None,
    #                 stop_on_error=False, collect_report=True, **options):
    #     return self.assert_it(self.assertTrue, (current_result,), output_success_msg, output_failed_msg,
    #                           checkpoint_description=checkpoint_description, method_name=inspect.stack()[0][3],
    #                           **options)
    #
    # def assert_false(self, current_result, output_success_msg=None, output_failed_msg=None, checkpoint_description=None,
    #                  stop_on_error=False, collect_report=True, **options):
    #     return self.assert_it(self.assertFalse, (current_result,), output_success_msg, output_failed_msg,
    #                           checkpoint_description=checkpoint_description, method_name=inspect.stack()[0][3],
    #                           **options)
    #
    # def assert_in(self, current_result, in_list, output_success_msg=None, output_failed_msg=None,
    #               checkpoint_description=None, stop_on_error=False, collect_report=True, **options):
    #     return self.assert_it(self.assertIn, (current_result, in_list), output_success_msg, output_failed_msg,
    #                           checkpoint_description=checkpoint_description, method_name=inspect.stack()[0][3],
    #                           **options)
    #
    # def assert_notin(self, current_result, in_list, output_success_msg=None, output_failed_msg=None,
    #                  checkpoint_description=None, stop_on_error=False, collect_report=True, **options):
    #     return self.assert_it(self.assertNotIn, (current_result, in_list), output_success_msg, output_failed_msg,
    #                           checkpoint_description=checkpoint_description, method_name=inspect.stack()[0][3],
    #                           **options)
    #
    # def assert_dict_contains(self, subnet, dictionary, output_success_msg=None, output_failed_msg=None,
    #                          checkpoint_description=None, stop_on_error=False, collect_report=True, **options):
    #     if isinstance(dictionary, Bunch):
    #         dictionary = {"statusCode": dictionary['statusCode'],
    #                       "responseBody": dictionary['responseBody']}
    #     return self.assert_it(self._assert_dict_contains, (subnet, dictionary), output_success_msg=output_success_msg,
    #                           output_failed_msg=output_failed_msg, checkpoint_description=checkpoint_description,
    #                           method_name=inspect.stack()[0][3], **options)
    #
    # def _assert_dict_contains(self, subnet, dictionary, ignore_compare_order=False):
    #
    #     '''
    #     compare 2 dict
    #     '''
    #
    #     def string2unicode(innest_dict):
    #         for k, v in innest_dict.items():
    #             if isinstance(v, str):
    #                 innest_dict[k] = v
    #             elif isinstance(v, list) and all(isinstance(item, str) for item in v):
    #                 innest_dict[k] = [v_str for v_str in v]
    #         return innest_dict
    #
    #     subnet = dict_format(subnet, string2unicode)
    #     dictionary = dict_format(dictionary, string2unicode)
    #     comparedResultDetail = DeepDiff(subnet, dictionary, ignore_order=ignore_compare_order, ignoreAdded=True,
    #                                     verbose_level=2)
    #     if comparedResultDetail != {}:
    #         comparedResultDetail = dict_format(comparedResultDetail, change_dict_key_pattern,
    #                                            ("values_changed", "hehe"))
    #         comparedResultDetail = dict_format(comparedResultDetail, change_dict_key_pattern,
    #                                            ("new_value", "actual_value"))
    #         #         comparedResultDetail = dict_format(comparedResultDetail, change_dict_key_pattern,("responseBody", ""))
    #         #         comparedResultDetail = dict_format(comparedResultDetail, change_dict_key_pattern,("root[","["))
    #         comparedResultDetail = dict_format(comparedResultDetail, change_dict_key_pattern,
    #                                            ("old_value", "expected_value"))
    #     comparedResultDetail = exclude_str_root(comparedResultDetail)
    #     # print comparedResultDetail=={},json.dumps(comparedResultDetail,indent=4)
    #     #     if comparedResultDetail != {}:
    #     #         generateTime().generate_time(json.dumps(comparedResultDetail, indent=4))
    #     #     else:
    #     #         pass
    #     if comparedResultDetail != {}:
    #         self.fail(json.dumps(comparedResultDetail, indent=4))
    #
    # def assert_to_fail(self, message, checkpoint_description=None, stop_on_error=False, collect_report=True):
    #     #         return self.fail(message)
    #     return self.assert_it(self.fail, (message,))
    #
    # def assert_to_pass(self, message, checkpoint_description=None, stop_on_error=False, collect_report=True):
    #     return self.assertTrue(True, message)

    def assert_it(self, assert_func, assert_params, output_failed_msg=None,
                  checkpoint_description=None, method_name=None, **options):

        print(checkpoint_description)

        _print = True
        if method_name:
            the_method_name = method_name
        else:
            the_method_name = assert_func.__name__

        if options:
            if 'get_log' in options:
                get_log = options['get_log']
            if 'subfolder_name' in options:
                subfolder_name = options['subfolder_name']
            if '_print' in options:
                _print = options['_print']

        # current_result, expected_result
        if len(assert_params) == 1:
            unitary = True
            current_result = assert_params[0]
        elif len(assert_params) == 2:
            unitary = False
            current_result = assert_params[0]
            expected_result = assert_params[1]

        try:
            assert_func(*assert_params, **options)

            output_success_msg = ""
            if True:
                if unitary:
                    print("[Checkpoint] - [Pass]: %s .[%s] success, current result: [%s]" % (
                        output_success_msg, the_method_name, current_result))
                else:
                    if assert_func.__name__ in ['assertIn', 'assertNotIn']:
                        if type(current_result) == str:
                            if assert_func.__name__ == "assertIn":
                                print(
                                    "[Checkpoint] - [Pass]: %s .[%s] success, expected result: [%s] in string: [%s]" % (
                                        output_success_msg, the_method_name, current_result, expected_result))
                            else:
                                print(
                                    "[Checkpoint] - [Pass]: %s .[%s] success, expected result: [%s] not in string: [%s]" % (
                                        output_success_msg, the_method_name, current_result, expected_result))
                        else:
                            print("[Checkpoint] - [Pass]: %s .[%s] success, expected result: [%s], in_list: [%s]" % (
                                output_success_msg, the_method_name, current_result, ' '.join(expected_result)))
                    else:
                        print(
                            "[Checkpoint] - [Pass]: %s . [%s] success, current result: [%s], expected result: [%s]" % (
                                output_success_msg, the_method_name, current_result, expected_result))
        except AssertionError as error:
            if output_failed_msg:
                print(output_failed_msg)
            else:
                output_failed_msg = ""

            if unitary:
                print("[Checkpoint] - [Fail]: %s . [%s] failed, current result: [%s]" % (
                    output_failed_msg, the_method_name, current_result))
            else:
                if assert_func.__name__ in ['assertIn', 'assertNotIn']:
                    if type(current_result) == str:
                        if assert_func.__name__ == "assertIn":
                            print(
                                "[Checkpoint] - [Fail]: %s . [%s] failed, expected result: [%s] not in string: [%s]" % (
                                    output_failed_msg, the_method_name, current_result, expected_result))
                        else:

                            print("[Checkpoint] - [Fail]: %s . [%s] failed, expected result: [%s] in string: [%s]" % (
                                output_failed_msg, the_method_name, current_result, expected_result))
                    else:
                        print("[Checkpoint] - [Fail]: %s . [%s] failed, current result: [%s], in_list: [%s]" % (
                            output_failed_msg, the_method_name, current_result, ' '.join(expected_result)))
                else:
                    print("[Checkpoint] - [Fail]: %s . [%s] failed, current result: [%s], expected result: [%s]" % (
                        output_failed_msg, the_method_name, current_result, expected_result))
            raise error



def get_testdata(file_path, function_name):
    test_data_path = file_path.replace("cases", "testdata").replace(".py", ".json")

    expr_with_testcase = "$..%s" % function_name.lower()
    testdata = jsonFile_get(test_data_path, expr_with_testcase)

    return testdata
