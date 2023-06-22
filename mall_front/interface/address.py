from interface.member import MemberInterface
from utils.send_method import SendMethod


class AddressInterface:
    def __init__(self, headers):
        self.url = 'http://47.108.206.100:8085'
        self.headers = headers

    def add_address(self):
        # 新增收货地址
        method = 'post'
        url = self.url + '/member/address/add'
        json = {
            "city": "武汉",
            "defaultStatus": 0,
            "detailAddress": "源码时代",
            "id": 0,
            "memberId": 5602,
            "name": "ldk",
            "phoneNumber": "15212345678",
            "postCode": "432100",
            "province": "湖北",
            "region": "东湖高新"
        }
        return SendMethod.send_method(method, url, json=json, headers=self.headers)


if __name__ == '__main__':
    member = MemberInterface()
    body = {
        "username": "ldk",
        "password": "123456"
    }
    headers = member.get_token(body)
    add = AddressInterface(headers)
    print(add.add_address())
