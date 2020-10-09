from urllib import parse
from urllib.request import urlopen, Request

base_url = 'http://cn.bing.com/search'
d = dict(q='马哥教育')

# # GET
# url = 'http://www.magedu.com/python?id=1&name=tom'
# # POST
# url = 'http://www.magedu.com/python'
# body = 'id=1&name=tom'
u = parse.urlencode(d)
url = '{}?{}'.format(base_url, u)

print(u)
print(parse.unquote(url))
ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
     'Safari/537.36'

req = Request(url, headers={
    'User-agent': ua
})
with urlopen(req) as res:
    with open('a.html', 'wb+') as file:
        file.write(res.read())
        file.flush()
