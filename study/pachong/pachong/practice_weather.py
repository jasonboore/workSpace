from bs4 import BeautifulSoup
import requests
import bs4

def getHTMLText(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        response.encoding = response.apparent_encoding
        return response.text
    except:
        return "没找到！"

def fillList(weaList, html):
    soup = BeautifulSoup(html, 'html.parser')
    sd_weather = soup.find('div', id='7d').find('ul')
    # print(sd_weather.find('li'))
    for li in sd_weather:
        if isinstance(li, bs4.element.Tag):
            day = li('h1')[0].string
            status = li(name='p', attrs={'class':'wea'})[0].string
            tem = li.find(name='p', attrs={'class':'tem'}).i.string
            win = li.find(name='p', attrs={'class':'win'})
            wind = win.em.span['title']
            wind_level = win.i.string
            weaList.append([day, status, tem, wind, wind_level])


def printWeather(weaList, city):
    print('=' * 38, city + '7日天气预报', '=' * 38)
    form = "\t{:16}\t{:16}\t{:16}\t{:16}\t{:16}"
    print(form.format('<日期>', '<天气>', '<温度>', '<风向>', '<风力>'))
    print(" " * 3, '-' * 88)
    for wea_day in weaList:
        print(form.format(wea_day[0],wea_day[1],wea_day[2],wea_day[3],wea_day[4]))


def main():
    weaList = []
    url = 'http://www.weather.com.cn/weather/101210101.shtml'
    html = getHTMLText(url)
    fillList(weaList, html)
    printWeather(weaList, '杭州')

main()
