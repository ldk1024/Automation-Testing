from interface.member import MemberInterface
from utils.send_method import SendMethod
from pprint import pprint


class OrderInterface:
    def __init__(self, headers):
        self.url = 'http://47.108.206.100:8085'
        self.headers = headers

    def confirm_order(self, cart_id):
        # 确认订单
        method = 'post'
        url = self.url + '/order/generateConfirmOrder'
        json = [cart_id]
        return SendMethod.send_method(method, url, json=json, headers=self.headers)

    def generate_order(self, card_id):
        # 生成订单,不使用优惠券和积分
        method = 'post'
        url = self.url + '/order/generateOrder'
        json = {
            "cartIds": [
                card_id
            ],
            "memberReceiveAddressId": 715082,
            "payType": 2,
        }
        return SendMethod.send_method(method, url, json=json, headers=self.headers)

    def pay_success(self, order_id):
        # 支付成功回调
        method = 'post'
        url = self.url + '/order/paySuccess'
        data = {
            "orderId": order_id,
            "payType": 2
        }
        return SendMethod.send_method(method, url, data=data, headers=self.headers)


if __name__ == '__main__':
    member = MemberInterface()
    body = {
        "username": "ldk",
        "password": "123456"
    }
    headers = member.get_token(body)
    order = OrderInterface(headers)
    # pprint(order.confirm_order(9227))
    # pprint(order.generate_order(9227))
    print(order.pay_success(9641))
