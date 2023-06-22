import json


class OperationJson:
    @staticmethod
    def build_data(filepath):
        with open(filepath, mode='r', encoding='utf-8') as f:
            json_data = json.load(f)
        return json_data


if __name__ == '__main__':
    print(OperationJson.build_data('../data/login_data.json'))
