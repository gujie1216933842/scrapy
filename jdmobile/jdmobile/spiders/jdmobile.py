# Author:Bob
import scrapy
from jdmobile.items import JdmobileItem
from scrapy.http import Request


class jdmobile(scrapy.Spider):
    name = "jdmobile"
    allowed_domains = ["dangdang.com"]
    start_urls = (
        "http://book.dangdang.com/",
    )

    def parse(self, response):
        item = JdmobileItem()
        # 提取手机,xpath表达式
        item['title'] = response.xpath('//a[@name="itemlist-picture"]/@title').extract() #书名
        item['price'] = response.xpath('//span[@class="search_now_price"]/text()').extract() #价格
        item['comment_count'] = response.xpath('//a[@class="search_comment_num"]/text()').extract() #评论数
        item['author'] = response.xpath('//a[@name="itemlist-author"]/@title').extract() #作者
        item['publicing_company'] = response.xpath('//a[@name="P_cbs"]/@title').extract() #出版社
        yield item

        for i in range(1, 100):  # range的范围
            url = "http://search.dangdang.com/?key=it&act=input&category_path=01.00.00.00.00.00&type=01.00.00.00.00.00&page_index=" + str(
                i) + "#J_tab"
            #print(url)
            yield Request(url, callback=self.parse)
