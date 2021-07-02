from dataclasses import dataclass

import pytest


def pytest_generate_tests(metafunc):
    # called once per each test function
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = list(funcarglist[0])
    args = [[funcargs[name] for name in argnames] for funcargs in funcarglist]
    metafunc.parametrize(argnames, args)


@dataclass
class test_equals:
    a: int
    b: int


testdata1 = test_equals(a=1, b=2)
testdata2 = test_equals(a=3, b=4)


class TestClass:
    # a map specifying multiple argument sets for a test method
    params = {
        'test_equals': [testdata1.__dict__, testdata2.__dict__],
        'test_zerodivision': [dict(a=1, b=0), ],
    }

    def test_equals(self, a, b):
        print(a, b)
        # assert a == b

    def test_zerodivision(self, a, b):
        pytest.raises(ZeroDivisionError)
