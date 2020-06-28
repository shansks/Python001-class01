# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MaoyanspiderPipeline(object):
    def process_item(self, item, spider):
        title = item['title']
        type = item['type']
        date = item['date']
        output = f'{title},{type},{date}|\n\n'
        with open('./doubanmovie.csv', 'a+', encoding='utf-8') as article:
            article.write(output)
        return item
