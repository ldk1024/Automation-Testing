import pytest

from utils.get_keyword import GetKeyword
from utils.oper_database import DBTools


class TestShopping:
    def test_shopping(self, cart, order):
        # 检查库存
        stock_sql = 'select stock from pms_sku_stock where id = 99;'
        stock_before = GetKeyword.get_keyword(DBTools.select_one(stock_sql), 'stock')
        print(f'购买前的库存:{stock_before}')
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
        # 添加购物车
        cart.cart_add(cart_body)
        # 购物车表中查找购物车记录ID和软删除状态,添加购物车,确认订单但是未生成订单时状态为0,生成订单后变为1
        cart_sql = 'select id,delete_status from oms_cart_item where member_id=5602 order by create_date desc;'
        delete_status = GetKeyword.get_keyword(DBTools.select_one(cart_sql), 'delete_status')
        # 获取购物车记录ID
        cart_id = GetKeyword.get_keyword(DBTools.select_one(cart_sql), 'id')
        pytest.assume(delete_status == 0)
        # 确认订单
        confirm_result = order.confirm_order(cart_id)
        # 获取购物车列表信息
        cartPromotionItemList = GetKeyword.get_keyword(confirm_result, 'cartPromotionItemList')
        pytest.assume(cartPromotionItemList is not None)
        # 获取收货地址信息
        memberReceiveAddressList = GetKeyword.get_keyword(confirm_result, 'memberReceiveAddressList')
        pytest.assume(memberReceiveAddressList is not None)
        # 获取金额
        totalAmount = GetKeyword.get_keyword(confirm_result, 'totalAmount')  # 总金额
        freightAmount = GetKeyword.get_keyword(confirm_result, 'freightAmount')  # 运费
        promotionAmount = GetKeyword.get_keyword(confirm_result, 'promotionAmount')  # 优惠金额
        payAmount = GetKeyword.get_keyword(confirm_result, 'payAmount')  # 实付金额
        # 断言总金额=商品单价*商品数量
        pytest.assume(totalAmount == cart_body['price'] * cart_body['quantity'])
        # 断言实付金额=总金额+运费-优惠金额
        pytest.assume(payAmount == totalAmount + freightAmount - promotionAmount)
        # 生成订单
        order.generate_order(cart_id)
        # 从订单表中找到最新一条订单
        order_sql = 'select id,status from oms_order where member_id=5602 order by id desc;'
        # 判断status是否为0
        status_before = GetKeyword.get_keyword(DBTools.select_one(order_sql), 'status')
        pytest.assume(status_before == 0)
        # 断言购物车表中对应的软删除状态变为1
        delete_status = GetKeyword.get_keyword(DBTools.select_one(cart_sql), 'delete_status')
        pytest.assume(delete_status == 1)
        # 获取订单ID
        order_id = GetKeyword.get_keyword(DBTools.select_one(order_sql), 'id')
        # 支付成功回调
        order.pay_success(order_id)
        # 断言支付成功后的status=1
        status_after = GetKeyword.get_keyword(DBTools.select_one(order_sql), 'status')
        pytest.assume(status_after == 1)
        # 断言库存扣减情况
        stock_after = GetKeyword.get_keyword(DBTools.select_one(stock_sql), 'stock')
        pytest.assume(stock_before - stock_after == cart_body['quantity'])


if __name__ == '__main__':
    pytest.main(['-s', 'test_shopping.py'])
