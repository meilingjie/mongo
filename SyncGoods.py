# coding：utf-8

import requests


def sync():
    url = '******/sync-goods'

    params = {
        'goodsId': '6132'
    }

    re = requests.get(url, params)

    return re


if __name__ == '__main__':
    re = sync()
    print(re.status_code)
    print(str(re.content, 'utf-8'))
