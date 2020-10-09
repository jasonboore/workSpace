import urllib3
from urllib import parse
from urllib3.response import HTTPResponse
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
     'Safari/537.36'

jurl = 'https://movie.douban.com/j/search_subjects'

d = {
    'type': 'movie',
    'tag': '热门',
    'page_limit': 50,
    'page_start': 0
}
with urllib3.PoolManager() as http:
    response = http.request('GET', '{}?{}'.format(jurl, parse.urlencode(d)), headers={
        'User-agent': ua
    })
    print(type(response))
    print(response)
    # response:HTTPResponse = HTTPResponse()
    print(response.data)
    print(response.status)