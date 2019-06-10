# -*- coding: utf-8 -*-
import scrapy
from DoubanSpider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    start = 0
    url = 'https://movie.douban.com/top250?start='
    end = '&filter='
    start_url = [url + str(start) + end]

    def parse(self, response):
        item = DoubanspiderItem()
        movies = response.xpath("//div[@class='info']")
        for each in movies:
            title = each.xpath("div[@class='hd']/a/span[@class='title'][1]/text()").extract()
            content = each.xpath("div[@class='bd']/p/text()").extract()
            score = each.xpath("div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()
            info = each.xpath("div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract()

            item['title'] = title[0]
            item['content'] = content
            item['score'] = score[0]
            item['info'] = info[0]
            print(item)

            # 提交item,将数据传入piplines.py模块
            yield item

        if self.start <= (10-1)*25:
            self.start += 25
            next_url = self.url + str(self.start) + self.end
            yield scrapy.Request(next_url, callback=self.parse)

