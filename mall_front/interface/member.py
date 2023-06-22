from utils.send_method import SendMethod
from utils.get_keyword import GetKeyword
from pprint import pprint


class MemberInterface:
    def __init__(self):
        self.url = 'http://47.108.206.100:8085'

    def get_auth_code(self, telephone):
        # 获取验证码接口
        method = 'get'
        url = self.url + '/sso/getAuthCode'
        params = {'telephone': telephone}
        return SendMethod.send_method(method=method, url=url, params=params)

    def get_verify_code(self, telephone):
        # 获取验证码的值
        response = self.get_auth_code(telephone)
        return GetKeyword.get_keyword(response, 'data')

    def register(self, body):
        # 会员注册接口
        method = 'post'
        url = self.url + '/sso/register'
        return SendMethod.send_method(method=method, url=url, data=body)

    def login(self, body):
        # 会员登录接口
        method = 'post'
        url = self.url + '/sso/login'
        return SendMethod.send_method(method=method, url=url, data=body)

    def get_token(self, body):
        # 获取会员token
        response = self.login(body)
        token = GetKeyword.get_keyword(response, 'token')
        return {'Authorization': f'Bearer {token}'}

    def get_user_info(self, name, body):
        # 获取会员信息
        method = 'get'
        url = self.url + '/sso/info'
        params = {"name": name}
        headers = self.get_token(body)
        return SendMethod.send_method(method=method, url=url,
                                      params=params, headers=headers)

    def update_pwd(self, body):
        # 更新密码
        method = 'post'
        url = self.url + '/sso/updatePassword'
        return SendMethod.send_method(method=method, url=url, data=body)


if __name__ == '__main__':
    member = MemberInterface()
    telephone = '15212345678'
    # 会员注册
    # body = {
    #     "authCode": member.get_verify_code(telephone),
    #     "password": "123456",
    #     "telephone": telephone,
    #     "username": "ldk"
    # }
    # pprint(member.register(body))
    # 获取会员信息
    body = {
        "username": "ldk",
        "password": "123456"
    }
    pprint(member.get_user_info('ldk', body))
    # pprint(member.login(body))
    # 更新密码
    # body = {
    #     "authCode": member.get_verify_code(telephone),
    #     "password": "123456",
    #     "telephone": telephone
    # }
    # pprint(member.update_pwd(body))
