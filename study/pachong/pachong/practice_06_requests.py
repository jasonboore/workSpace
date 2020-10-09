# 推荐使用
import requests
from urllib import parse

ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
     'Safari/537.36'

jurl = 'https://movie.douban.com/j/search_subjects'

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 50,
    'page_start': 0
}

url = '{}?{}'.format(jurl, parse.urlencode(d))
response = requests.request('GET', url, headers={
    'User-agent': ua
})
with response:
    print(response.text)
    print(response.status_code)
    print(response.url)
    print(response.headers)
    print(response.request)