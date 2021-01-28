# check fixture execute with cmd '--setup-show'
import signal
from functools import wraps

import pytest
import pytest_rerunfailures

from lib.base_test_case import get_testdata
from _pytest.runner import runtestprotocol
from _pytest.runner import pytest_runtest_makereport


@pytest.fixture()
def some_data():
    return 22


@pytest.fixture(name="rename_fixture")
def some_data2():
    return 22


# @pytest.fixture(scope="session", autouse=True)
# def session_fixture():
#     print("session setup")
#     yield
#     print("session teardown")


# @pytest.fixture(scope="function")
# def my_fixture(tmpdir):
#     print("function setup")
#     yield
#     print("function teardown")


# def pytest_sessionstart(session):
#     print("session_start")
#
#
# def pytest_sessionfinish(session):
#     print("session_finish")

# 会在pytest自己的框架上包装，tryfirst=True 执行先执行自己的hook
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    # cur_result = result.setdefault(get_raw_id(item), {})
    # cur_result[len(cur_result) + 1] = {
    #     'setup': False,
    #     'call': False,
    #     'teardown': False,
    #     'start': t,
    #     'spend': 0
    # }
    # print("each test case:", item)
    set_signal()
    out = yield


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_call(item):
    set_signal()
    out = yield
    # release_signal()


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_teardown(item, nextitem):
    print(item, nextitem)
    set_signal()
    out = yield
    # release_signal()


#
#
# def pytest_configure(config):
#     print("start config")
#
#
# def pytest_cmdline_main(config):
#     print("cmdline")
#
#
# def pytest_runtest_protocol(item, nextitem):
#     print("runtest_protocol: ", item, nextitem)
#
#
# def pytest_runtest_logstart(nodeid, location):
#     print("runtest_logstart: ", nodeid, location)
#
#
# def pytest_runtest_setup(item):
#     print("runtest_setup: ", item)
#
# @pytest.hookimpl(hookwrapper=True, tryfirst=True)
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     rep = outcome.get_result()
#     setattr(item, "rep_" + rep.when, rep)
#     if rep.when == 'call':
#         if rep.failed:
#             pass
#             # ui test
#             # if browser_option.screen_shot:
#             #     report_dir = browser_option.report_dir
#             #     picture_name = item.name + '.png'
#             #     picture_path = join(report_dir, picture_name)
#             #     context.browser.save_screenshot(picture_path)


#
# def pytest_collectstart(collector):
#     '''collector starts collecting.'''
#     print(collector)
#
#
# def pytest_itemcollected(item):
#     '''we just collected a test item.'''
#     print(item)
#
#
# def pytest_collectreport(report):
#     '''collector finished collecting.'''
#     print(report)
#
#
# def pytest_runtest_logreport(report):
#     '''process a test setup/call/teardown report relating to the respective phase of executing a test.'''
#     print(report)

# def pytest_itemcollected(item):
#     # modify test case name
#     item._nodeid = item.nodeid + "\n"

def get_reruns_count(item):
    return 2


def get_reruns_delay(item):
    return 3


# 决定重试次数和时间
# pytest_rerunfailures.get_reruns_count = get_reruns_count
# pytest_rerunfailures.get_reruns_delay = get_reruns_delay

# do some ignore
# def pytest_ignore_collect(path, config):
#     if "cases" == path.basename:
#         return True  # true mean ignore
#     return False  # false mean collect


# def pytest_generate_tests(metafunc):
#     # called once per each test function
#     test_module_path = metafunc.module.__file__
#     function_name = metafunc.function.__name__
#     test_data = get_testdata(test_module_path, function_name)
#     # arg1=["case1_name","case2_name"]
#     # arg2=["case1_data","case2_data"]
#     """ [[1, 2], [3, 3]]"""
#     # metafunc.parametrize(arg1,arg2)
#     if not isinstance(test_data, list):
#         test_data = [test_data]
#     metafunc.parametrize(function_name, test_data)

# def pytest_collection_modifyitems(session, config, items):
#     """ called after collection is completed
#         you can modify the ``items`` list
#     """
#     print(session, config, items)

time_out = 5


def set_signal():
    signal.signal(signal.SIGALRM, timeout_func)
    signal.setitimer(signal.ITIMER_REAL, time_out)


def release_signal():
    signal.setitimer(signal.ITIMER_REAL, 0)
    signal.signal(signal.SIGALRM, signal.SIG_DFL)


def timeout_func(signum, frame):
    pytest.fail('用例运行超时，当前超时时间设置为{}秒'.format(time_out))
