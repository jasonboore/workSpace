import random
from urllib.request import urlopen, Request

url = 'http://www.bing.com'
ua_list = ['Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
           'Safari/537.36 ', 'User-Agent:Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, '
                             'like Gecko) Version/5.1 Safari/534.50','User-Agent:Mozilla/5.0 (compatible; MSIE 9.0; '
                                                                     'Windows NT 6.1; Trident/5.0']
user_agent = random.choice(ua_list)

req = Request(url, headers={'User-agent': user_agent})
# req.add_header('User-agent': user_agent)
# GET
response = urlopen(req, timeout=5)
print(response.closed)
with response:
    print(type(response))
    print(response.status)
    print(response._method)
    # 获得header
    print(response.info())
    print(response.read())
    print(response.geturl())
print(req.get_header('User-agent'))
print(response.closed)
