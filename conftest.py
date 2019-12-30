# check fixture execute with cmd '--setup-show'
import pytest


# fixture return data
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


def pytest_sessionstart(session):
    print("session_start")


def pytest_sessionfinish(session):
    print("session_finish")
