import pytest


def test1(some_data):
    assert some_data == 22


def test2(rename_fixture):
    assert rename_fixture == 22
