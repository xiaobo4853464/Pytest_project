import pytest

# 测试账号数据
test_user_data = ["admin1", "admin2"]


@pytest.fixture(scope="module")
def login(request):
    user = request.param
    print("pre:", user)
    yield user
    print("post:", user)


class TestParam2fixture(object):
    @pytest.mark.parametrize("login", test_user_data, indirect=True)  # 添加indirect=True参数是为了把login当成一个函数去执行，而不是一个参数
    def test_login(self, login):
        """test case"""
        u = login
        print("process", u)
