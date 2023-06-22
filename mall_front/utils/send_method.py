import requests


class SendMethod:
    @staticmethod
    def send_method(method, url, params=None, data=None, json=None, headers=None):
        # 封装请求
        if method in ['get', 'post']:
            response = requests.request(method=method, url=url, params=params,
                                        data=data, json=json, headers=headers)
        else:
            response = None
            print('请求方法错误')

        # 封装响应
        result = {}
        if response is not None:
            result['status_code'] = response.status_code
            result['headers'] = response.headers
            result['body'] = response.json()
            result['response_time'] = int(response.elapsed.microseconds / 1000)
            return result

        else:
            return response


if __name__ == '__main__':
    method = 'post'
    url = 'http://47.108.206.100:8080/admin/login'
    body = {
        "username": "admin",
        "password": "macro123"
    }
    print(SendMethod.send_method(method=method, url=url, json=body))
