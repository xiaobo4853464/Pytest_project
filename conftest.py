# check fixture execute with cmd '--setup-show'
from functools import wraps

import pytest


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


@pytest.fixture(scope="function")
def my_fixture(tmpdir):
    print("function setup")
    yield
    print("function teardown")


# def pytest_sessionstart(session):
#     print("session_start")
#
#
# def pytest_sessionfinish(session):
#     print("session_finish")

def pytest_runtest_setup(item):
    # called for running each test in 'a' directory
    print("each test case:", item)


def pytest_configure(config):
    print("start config")


def pytest_cmdline_main(config):
    print("cmdline")


def pytest_runtest_protocol(item, nextitem):
    print("runtest_protocol: ", item, nextitem)


def pytest_runtest_logstart(nodeid, location):
    print("runtest_logstart: ", nodeid, location)


def pytest_runtest_setup(item):
    print("runtest_setup: ", item)


def pytest_runtest_call(item):
    print("runtest_call: ", item)


def pytest_runtest_teardown(item):
    print("runtest_teardown: ", item)


def pytest_runtest_teardown(item, nextitem):
    print("pytest_runtest_teardown:", item, nextitem)


def pytest_runtest_makereport(item, call):
    print("runtest_makereport: ", item, call)


def pytest_collectstart(collector):
    '''collector starts collecting.'''
    print(collector)


def pytest_itemcollected(item):
    '''we just collected a test item.'''
    print(item)


def pytest_collectreport(report):
    '''collector finished collecting.'''
    print(report)


def pytest_runtest_logreport(report):
    '''process a test setup/call/teardown report relating to the respective phase of executing a test.'''
    print(report)
