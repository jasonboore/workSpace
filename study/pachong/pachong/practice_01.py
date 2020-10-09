from urllib import parse
from urllib.request import urlopen, Request
import simplejson

url = 'http://httpbin.org/post'
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
     'Safari/537.36'
d = dict(name='张三，@=/&*', age='6')
data = parse.urlencode(d)
req = Request(url)
req.add_header(key='User-agent', val=ua)

# POST请求
# encode()对url进行编码
with urlopen(req, data=data.encode()) as res:
    text = res.read()
    dic = simplejson.loads(text)
    print(dic)