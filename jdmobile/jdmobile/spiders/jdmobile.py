# Author:Bob
import scrapy
from jdmobile.items import JdmobileItem
from scrapy.http import Request

class jdmobile(scrapy.Spider):
    name = "jdmobile"
    allowed_domains = ["baidu.com"]
    start_urls = (
        "https://www.jd.com/",
    )

    def parse(self, response):
        item = JdmobileItem()
        # 提取手机,xpath表达式
        item['title'] = response.xpath("//div[@class='p-name-type-2']/a/@title").extract()
        print(item['title'])
        yield item

        for i in range(1, 100):    #range的范围
            url = "https://search.jd.com/Search?keyword=%E6%89%8B%E6%9C%BA&enc=utf-8&qrst=1&rt=1" \
                  "&stop=1&vt=2&cid2=653&cid3=655&page=" + str(2 * i + 1) + "&s=&click=0"
            yield Request(url,callback=self.parse)
