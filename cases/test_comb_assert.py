import pytest
from pytest_assume.plugin import assume

# def test_add2():
#     # AssumeContextManager()(1 == 1)
#     # AssumeContextManager()(1 == 2)
#     # AssumeContextManager()(1 == 1)
#     # AssumeContextManager()(1 == 2)
#
#     # assert 1==2
#     # assert 1==1
#
#     assume(1 == 1)
#     assume(1 == 2)
#     assume(1 == 1)
#     assume(1 == 2)
#     print("测试完成")


list1 = [1,2,3]
list2 = [(1,3,3),(2,3,6),(3,6,18)]



def multi(a,b):
    return a*b


class TestParam:
    @pytest.mark.parametrize("r", list1)
    def test_1_multi(self,r):
        print(r)
        # assert multi(a,b) == c
