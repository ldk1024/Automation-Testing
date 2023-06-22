from interface.member import MemberInterface
from utils.send_method import SendMethod
from pprint import pprint


class CartInterface:
    def __init__(self, headers):
        self.url = 'http://47.108.206.100:8085'
        self.headers = headers

    def cart_add(self, body):
        # 添加到购物车
        method = 'post'
        url = self.url + '/cart/add'
        return SendMethod.send_method(method, url, json=body, headers=self.headers)


if __name__ == '__main__':
    member = MemberInterface()
    body = {
        "username": "ldk",
        "password": "123456"
    }
    headers = member.get_token(body)
    cart = CartInterface(headers)
    cart_body = {
        "createDate": "2023-06-14T03:25:38.114Z",
        "deleteStatus": 0,
        "id": 0,
        "modifyDate": "2023-06-14T03:25:38.114Z",
        "quantity": 2,
        "memberId": 5602,
        "memberNickname": "ldk",
        "price": 2999,
        "productAttr": '[{"key":"颜色","value":"黑色"},{"key":"容量","value":"64G"}]',
        "productBrand": "小米",
        "productCategoryId": 19,
        "productId": 27,
        "productName": "小米8 全面屏游戏智能手机 6GB+64GB 黑色 全网通4G 双卡双待",
        "productPic": "http://macro-oss.oss-cn-shenzhen.aliyuncs.com/mall/images/20180615/xiaomi.jpg",
        "productSkuCode": "201808270027002",
        "productSkuId": 99,
        "productSn": "7437788",
        "productSubTitle": "骁龙845处理器，红外人脸解锁，AI变焦双摄，AI语音助手小米6X低至1299，点击抢购",
    }
    pprint(cart.cart_add(cart_body))
