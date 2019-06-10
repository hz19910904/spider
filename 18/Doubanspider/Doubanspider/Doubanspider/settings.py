# -*- coding: utf-8 -*-

BOT_NAME = 'Doubanspider'

SPIDER_MODULES = ['Doubanspider.spiders']
NEWSPIDER_MODULE = 'Doubanspider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.116 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False


DOWNLOAD_DELAY = 1

ITEM_PIPELINES = {
   'Doubanspider.pipelines.DoubanspiderPipeline': 300,
}

# MONGODB 主机环回地址127.0.0.1
MONGODB_HOST = '127.0.0.1'
# 端口号，默认是27017
MONGODB_PORT = 27017
# 设置数据库名称
MONGODB_DBNAME = 'DouBan'
# 存放本次数据的表名称
MONGODB_DOCNAME = 'DouBanMovies'

