from pytest_assume.plugin import assume

def test_add2():
    # AssumeContextManager()(1 == 1)
    # AssumeContextManager()(1 == 2)
    # AssumeContextManager()(1 == 1)
    # AssumeContextManager()(1 == 2)

    # assert 1==2
    # assert 1==1

    assume(1 == 1)
    assume(1 == 2)
    assume(1 == 1)
    assume(1 == 2)
    print("测试完成")
