import jsonpath


class GetKeyword:
    @staticmethod
    def get_keyword(source_data, keyword):
        try:
            return jsonpath.jsonpath(source_data, f'$..{keyword}')[0]
        except:
            print(f'关键字{keyword}不存在')
            return False

    @staticmethod
    def get_keywords(source_data, keyword):
        return jsonpath.jsonpath(source_data, f'$..{keyword}')


if __name__ == '__main__':
    data = {'status_code': 200,
            'headers': {'Vary': 'Origin'},
            'body': {'code': 200, 'message': '操作成功', 'data': {'id': 5602, 'memberLevelId': 4, 'username': 'ldk',
                                                              'password': '$2a',
                                                              'phone': '15212345678', 'status': 1,
                                                              'createTime': '2023-06-13T03:06:42.000+00:00'}},
            'response_time': 45}
    print(GetKeyword.get_keyword(data, 'id'))
