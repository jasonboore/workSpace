import requests
from urllib import parse
import re


def getHTMLText(url, ua):
    try:
        res = requests.request('GET', url, headers={
            'User-agent': ua
        })
        res.raise_for_status()
        res.encoding = res.apparent_encoding
        return res.text
    except:
        return ""


def parsePage(ilt, html):
    try:
        # 正则表达式获得价格
        print(html)
        plt = re.findall(r'\"view_price\"\:\"[\d\.]*]\"', html)
        print(plt)
        # 最小匹配 获得商品名
        tlt = re.findall(r'\"raw_title\"\:\"\.*?\"')
        for i in range(len(plt)):
            price = eval(plt[i].split(':')[1])
            title = eval(tlt[i].split(':')[1])
            ilt.append([price, title])
    except:
        print('')


def printGoodList(ilt):
    tplt = "{:4}\t{:8}\t{:16}"
    print(tplt.format('序号', '价格', '商品名称'))
    count = 0
    for g in ilt:
        count = count + 1
        print(tplt.format(count, g[0], g[1]))


def main():
    goods = '书包'
    depth = 2
    ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 ' \
         'Safari/537.36'
    start_url = 'http://s.taobao.com/search'

    infoList = []
    for i in range(depth):
        try:
            d = dict(d=goods, s=str(44 * i))
            url = '{}?{}'.format(start_url, parse.urlencode(d))
            html = getHTMLText(url, ua)
            parsePage(infoList, html)
        except:
            continue
    printGoodList(infoList)


main()
