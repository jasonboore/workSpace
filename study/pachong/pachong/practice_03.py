import time
from urllib import parse
from urllib.request import Request, urlopen
import simplejson
import pprint


def douban(page_limit=50, page_start=0):
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
         'Safari/537.36'

    jurl = 'https://movie.douban.com/j/search_subjects'

    d = {
        'type': 'movie',
        'tag': '热门',
        'page_limit': page_limit,
        'page_start': page_start
    }
    req = Request('{}?{}'.format(jurl, parse.urlencode(d)))
    req.add_header(key='User-agent', val=ua)
    with urlopen(req) as res:
        subjects = simplejson.loads(res.read())
        print(len(subjects['subjects']))
        return subjects['subjects']


list = []
i = 0
while True:
    db_list = douban(50, i)
    if not db_list:
        break
    list.extend(db_list)
    i += 50
    time.sleep(0.01)
pprint.pprint(list)
print(len(list))
