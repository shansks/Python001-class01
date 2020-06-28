# -*- coding: utf-8 -*-
import scrapy
import lxml.etree
from scrapy.selector import Selector
from MaoyanSpider.items import MaoyanspiderItem


class MoviespiderSpider(scrapy.Spider):
    name = 'moviespider'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3']

    # def parse(self, response):
    #     pass

    def start_requests(self):
        for i in range(0,1):
            url = f'https://maoyan.com/films?showType=3&offset={i*30}'
            yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        print(response.url)
        movies = Selector(response=response).xpath('//div[@class="movie-hover-info"]')
        for movie in movies:
            item = MaoyanspiderItem()
            title = movie.xpath('./div[@class="movie-hover-title"]/span/text()').extract_first()
            type = (movie.xpath('./div[@class="movie-hover-title"]/text()').extract()[4]).replace('\n','').strip(' ')
            date = (movie.xpath('./div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1]).replace('\n','').strip(' ')
            print('title:', title)
            print('type:',type)
            print('date:', date)
            item['title']=title
            item['type']=type
            item['date']=date
            yield item

