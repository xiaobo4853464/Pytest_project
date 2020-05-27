import pytest


@pytest.fixture(scope="session", autouse=True)
def session_fixture():
    pass


@pytest.fixture(scope="module", autouse=True)
def module_fixture():
    pass


@pytest.fixture(scope="class", autouse=True)
def class_fixture():
    pass


@pytest.fixture(scope="class")
def class_fixture2():
    print("class fixture2")


@pytest.fixture(scope="function", autouse=True)
def function_fixture(class_fixture2):  # 允许低级别的fixture调高级别的fixture，如function fixture可以调用所有fixture反之不行
    pass


class TestA(object):
    def test1(self):
        pass


class TestB(object):
    def test2(self):
        pass
