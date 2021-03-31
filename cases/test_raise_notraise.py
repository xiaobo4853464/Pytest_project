import pytest

from contextlib import contextmanager


def get_exception():
    raise TypeError


def get_no_exception():
    pass


@contextmanager
def not_raises(e):
    try:
        yield
    except e:
        raise pytest.fail("DID RAISE {}".format(repr(e)))


class TestRaiseNotRaise(object):
    def test_raise(self):
        with pytest.raises(TypeError):
            get_exception()

    def test_not_raise(self):
        with not_raises(TypeError):
            get_no_exception()
