import requests
from urllib import parse

urls = ['http://www.baidu.com/s?wd=magedu', 'http://www.baidu.com/s?wd=magedu']

session = requests.Session()
with session:
    for url in urls:
        response = session.get(url, headers={
            'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
                        'Safari/537.36'
        })
        with response:
            print(response.text[:50])
            print('-' * 30)
            print(response.cookies)
            print('-' * 30)
            print(response.headers)


