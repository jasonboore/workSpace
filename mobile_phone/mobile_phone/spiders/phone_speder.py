import scrapy


class PhoneSpider(scrapy.Spider):
    name = 'phone'
    start_urls = ['https://www.jihaoba.com/escrow/']
    i = 0
    def parse(self, response):
        print(PhoneSpider.i)
        PhoneSpider.i += 1
        for ul in response.xpath('//div[@class="numbershow"]/ul'):
            # 1.第一种
            # number = ul.xpath('li[contains(@class,"number")]/a/text()').extract()
            # end = ul.xpath('li[contains(@class,"number")]/a/span/text()').extract()
            # if len(end):
            #     number[0] = number[0] + end[0]
            # print(number[0])
            number = ul.xpath('./li[contains(@class,"number")]/a/@href').re('\d{11}')[0]
            price = ul.xpath('./li[contains(@class,"price")]/span/text()').extract_first()[1:]
            if price.endswith('万'):
                price = int(float(price[:-1]) * 10000)
            else:
                price = int(price)
            yield {
                'phone': number,
                'price': price
            }
        # 请求下一页，请求下一个url
        next = 'https://www.jihaoba.com' + response.xpath('//a[@class="m-pages-next"]/@href').extract_first()
        yield scrapy.Request(next)
