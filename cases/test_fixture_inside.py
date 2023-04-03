import pytest


@pytest.fixture
def login():
    return 'token'


# 这里在执行setup时，就会先去执行login函数，这里就是fixture函数调用另一个fixture函数
@pytest.fixture
def setup(login):
    return 'my:' + login


def test_demo(setup):
    assert setup == 'my:token'
