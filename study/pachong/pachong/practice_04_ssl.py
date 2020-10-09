from urllib.request import urlopen, Request
import ssl

url = 'http://www.12306.cn/mormhweb'
req = Request(url)
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
         'Safari/537.36'
req.add_header(key='User-agent', val=ua)
# 忽略不信任的证书
context = ssl._create_default_https_context()
with urlopen(req) as res:
    print(res._method)
    print(res.read())
