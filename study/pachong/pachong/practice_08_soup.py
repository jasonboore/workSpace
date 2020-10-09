import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        # 2.通过requests进行数据请求
        r = requests.get(url, timeout=30)
        # 3.检验爬取是否成功
        r.raise_for_status()
        # 4.设置编码 utf-8
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return ""


def fillUnivList(uList, html):
    # 5. 解析html
    soup = BeautifulSoup(html, 'html.parser')
    # 6. 遍历想要的标签
    for tr in soup.find('tbody').children:
        # 过滤tr标签
        if isinstance(tr, bs4.element.Tag):
            tds = tr('td')
            uList.append([tds[0].string, tds[2].string, tds[4].string])



def printUnivList(uList, num):
    print("{:^10}\t{:^6}\t{:^10}".format('排名', '学校', '得分'))
    for i in range(num):
        u = uList[i]
        print(u)
        print("{:^10}\t{:^6}\t{:^10}".format(u[0], u[1], u[2]))


def main():
    uinfo = []
    # 1.设置url
    url = 'http://www.shanghairanking.cn/rankings/bcur/2020'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    print(uinfo)
    printUnivList(uinfo, 20)

main()
