import os
import pytest

from interface.member import MemberInterface
from utils.get_keyword import GetKeyword
from utils.oper_json import OperationJson


class TestMemberLogin:
    # 登录测试用例
    file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'data', 'login_data.json')

    @pytest.mark.parametrize('test_data', OperationJson.build_data(file_path))
    def test_login(self, test_data):
        # 准备测试数据
        body = {
            "username": test_data.get("username"),
            "password": test_data.get("password")
        }
        # 调用接口层的相关方法发送请求
        resp = MemberInterface().login(body)
        # 对响应结果断言
        assert GetKeyword.get_keyword(resp, 'status_code') == test_data.get('status_code')
        assert GetKeyword.get_keyword(resp, 'code') == test_data.get('code')
        assert GetKeyword.get_keyword(resp, 'message') == test_data.get('message')


if __name__ == '__main__':
    pytest.main(['-s', 'test_login.py'])
