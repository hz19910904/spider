# -*- coding: utf-8 -*-
import scrapy
from Doubanspider.items import DoubanspiderItem


class DoubanSpider(scrapy.Spider):
    name = 'douban'  # 这个爬虫的识别名称，必须是唯一的，在不同的爬虫必须定义不同的名字
    allowed_domains = ['movie.douban.com']   # 是搜索的域名范围，也就是爬虫的约束区域，规定爬虫只爬取这个域名下的网页，不存在的URL会被忽略
    start = 0
    url = 'https://movie.douban.com/top250?start='
    end = '&filter='
    start_urls = [url + str(start) + end]  # 爬取的URL元祖/列表。爬虫从这里开始抓取数据，所以，第一次下载的数据将会从这些urls开始。其他子URL将会从这些起始URL中继承性生成

    def parse(self, response):
        """
        解析的方法，每个初始URL完成下载后将被调用，调用的时候传入从每一个URL传回的Response对象来作为唯一参数，主要作用如下:
        1. 负责解析返回的网页数据(response.body)，提取结构化数据(生成item)
        2. 生成需要下一页的URL请求。
        :param response:
        :return:
        """

        # 将我们得到的数据封装到一个 `DoubanspiderItem` 对象
        item = DoubanspiderItem()

        movies = response.xpath("//div[@class='info']")

        for each in movies:
            # extract()方法返回的都是unicode字符串
            title = each.xpath('div[@class="hd"]/a/span[@class="title"]/text()').extract()
            content = each.xpath('div[@class="bd"]/p/text()').extract()
            score = each.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()
            info = each.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()

            # 去除字符串中的\n,\t,\xa0等空字符
            # join()： 连接字符串数组。将字符串、元组、列表中的元素以指定的字符(分隔符)连接生成一个新的字符串。
            # split():split方法中不带参数时，表示分割所有换行符、制表符、空格。
            item['title'] = title[0].strip()
            item['content'] = "".join(content[0].split())
            item['score'] = score[0].strip()
            item['info'] = info[0].strip()

            # 将获取的数据交给pipelines
            yield item

        if self.start <= 225:
            self.start += 25
            """
            url: 就是需要请求，并进行下一步处理的url
            callback: 指定该请求返回的Response，由那个函数来处理。
            """
            yield scrapy.Request(self.url + str(self.start) + self.end, callback=self.parse)
