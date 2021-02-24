from cases.mock.objs import PayApi


class TestPayApi(object):

    def test_success(self, mocker):
        pay = PayApi()
        print(pay.auth(1, 2))
        pay.auth = mocker.Mock(return_value={'status_code': '200'}, side_effect={"status_code": 404})
        status = pay.pay('1000', '12345', '10000')
        print(pay.auth(1, 2))
        print(status)
        assert status == '支付成功'

    def test_fail(self, mocker):
        pay = PayApi()
        pay.auth = mocker.Mock(return_value={'status_code': '500'})
        status = pay.pay('1000', '12345', '10000')
        assert status == '支付失败'

    def test_error(self, mocker):
        pay = PayApi()
        pay.auth = mocker.Mock(return_value={'status_code': '300'})
        status = pay.pay('1000', '12345', '10000')
        assert status == '未知错误'

    def test_exception(self, mocker):
        pay = PayApi()
        pay.auth = mocker.Mock(return_value='200')
        status = pay.pay('1000', '12345', '10000')
        assert status == 'Error, 服务器异常!'
