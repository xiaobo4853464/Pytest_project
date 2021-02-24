import requests


class PayApi(object):
    @staticmethod
    def auth(card, amount) -> dict:
        """
        第三方支付接口
        :param card: 卡号
        :param amount: 支付金额
        :return:
        """
        try:
            pay_url = "http://www.xiaobopay.com"  # 第三方支付接口地址
            data = {"card": card, "amount": amount}
            response = requests.post(pay_url, data=data)  # 请求第三方支付接口
            return response.json()  # 返回状态码
        except Exception as e :
            return {"error":"blocked"}

    def pay(self, user_id, card, amount):
        """
        我们自己的支付接口
        :param user_id: 用户id
        :param card: 卡号
        :param amount: 支付金额
        :return:
        """
        response = self.auth(card, amount)
        try:
            if response['status_code'] == '200':
                print('用户{}支付金额{}成功'.format(user_id, amount))
                return '支付成功'
            elif response['status_code'] == '500':
                print('用户{}支付失败, 金额不变'.format(user_id))
                return '支付失败'
            else:
                return '未知错误'
        except Exception:
            return "Error, 服务器异常!"
