# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class JdmobilePipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1",user="root",passwd="123",db="python_spider" ,charset="utf8")

        for i in range(0, len(item['title'])):
            title = item['title'][i]
            print(title)
            sql = " insert into jd_mobile (name,raw_add_time ) VALUES ( %s,now())" %(title)
            conn.query(sql)
            conn.close()
        return item
