# -*- coding: utf-8 -*-
import scrapy
from Doubanspider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'   # 爬虫名
    allowed_domains = ['movie.douban.com']  # 爬虫域
    start = 0
    url = 'https://movie.douban.com/top250?start='
    end = '&filter='
    start_urls = [url + str(start) + end]   # 开始爬取的URL元组, https://movie.douban.com/top250?start=0&filter=

    def parse(self, response):
        """
        1. 负责解析返回的网页数据,提取结构化数据(item)
        2. 生成下一个url请求
        :param response:
        :return:
        """
        # 负责解析返回的网页数据,提取结构化数据(item)

        # 讲我们得到的数据封装到一个'DoubanspiderItem'对象中
        item = DoubanspiderItem()

        movies = response.xpath("//div[@class='info']")

        for each in movies:
            # extract()返回一个列表
            title = each.xpath("div[@class='hd']/a/span[@class='title'][1]/text()").extract()
            content = each.xpath("div[@class='bd']/p[1]/text()").extract()
            score = each.xpath("div[@class='bd']/div[@class='star']/span[@class='rating_num']/text()").extract()
            info = each.xpath("div[@class='bd']/p[@class='quote']/span[@class='inq']/text()").extract()

            item['title'] = title[0].strip()
            item['content'] = "".join(content[0].split())
            item['score'] = score[0].strip()
            item['info'] = info[0].strip()

            # 将获取的数据传给piplines
            yield item

        # 获取下一页的url
        if self.start <= 225:
            self.start += 25
            next_url = self.url + str(self.start) + self.end
            yield scrapy.Request(next_url, callback=self.parse)

