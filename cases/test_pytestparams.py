import pytest


# pytest.param 用法
# 多组参数，其中的需要xfail或skip
@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    pytest.param("6*9", 42, marks=pytest.mark.xfail),
    pytest.param("0/0", 0, marks=pytest.mark.skip("除数不能为0")),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected
