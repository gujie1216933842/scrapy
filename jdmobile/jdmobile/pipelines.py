# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import re


class JdmobilePipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1", user="root", passwd="123", db="python_spider", charset="utf8")
        # 游标
        cursor = conn.cursor()
        for i in range(0, len(item['title'])):
            title = item['title'][i]
            price = item['price'][i]
            price = float(price[1:])

            comment_count = item['comment_count'][i]
            comment_count = int(comment_count[:-3])
            author = item['author'][i]
            publicing_company = item['publicing_company'][i]
            title = re.sub('\'', '', title)
            title = re.sub('\"', '', title)
            sql = " insert into dd_it_book (name,price,comment_count, author,publicing_company,raw_add_time) VALUES ( %s ,%s,%s,%s,%s,now())"
            cursor.execute(sql, (title, price, comment_count, author, publicing_company))
            conn.commit()
        cursor.close()
        conn.close()
        return item
