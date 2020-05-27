import pytest

# def test1(some_data):
#     assert some_data == 22
#
#
# def test2(rename_fixture):
#     assert rename_fixture == 22


import logging

logging.basicConfig(format='%(asctime)s - %(pathname)s[line:%(lineno)d] - %(levelname)s: %(message)s',
                    level=logging.WARNING)

l = logging.getLogger(__name__)


def test_1():
    l.debug('debug 信息')
    l.info('info 信息')
    l.warning('warning 信息')
    l.error('error 信息')
    l.critical('critial 信息')
