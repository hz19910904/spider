# -*- coding: utf-8 -*-

# Scrapy settings for Doubanspider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'Doubanspider'

SPIDER_MODULES = ['Doubanspider.spiders']
NEWSPIDER_MODULE = 'Doubanspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
   'Doubanspider.pipelines.DoubanspiderPipeline': 300,
}

MONGODB_HOST = '127.0.0.1'
MONGODB_PORT = 27017
MONGODB_DBNAME = 'DouBan'
MONGODB_DOCNAME = 'DouBanMoies'

