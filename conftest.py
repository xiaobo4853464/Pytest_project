# check fixture execute with cmd '--setup-show'
import pytest


# fixture return data
@pytest.fixture()
def some_data():
    return 22


@pytest.fixture(name="rename_fixture")
def some_data2():
    return 22


@pytest.fixture(scope="function")
def my_fixture(tmpdir):
    print("function setup")
    yield
    print("function teardown")
