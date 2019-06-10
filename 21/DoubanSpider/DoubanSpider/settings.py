# -*- coding: utf-8 -*-

# Scrapy settings for DoubanSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

# 项目名称
BOT_NAME = 'DoubanSpider'

# 搜索spider的模块列表
SPIDER_MODULES = ['DoubanSpider.spiders']
# 使用genspider的命令创建新spider的模块
NEWSPIDER_MODULE = 'DoubanSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
# 默认User-Agent
USER_AGENT = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36'

# Obey robots.txt rules
# robots.txt协议
ROBOTSTXT_OBEY = False

# 配置scrapy执行的最大并发请求
#CONCURRENT_REQUESTS = 32

# 下载延迟
#DOWNLOAD_DELAY = 3

# 下载延迟设置仅满足以下条件之一
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# 禁用cookies
COOKIES_ENABLED = False


# 禁用Talent控制台(默认启用)
#TELNETCONSOLE_ENABLED = False

# 请求头设置:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# 启用或禁用spider中间件
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'DoubanSpider.middlewares.DoubanspiderSpiderMiddleware': 543,
#}

# 启用或禁用下载中间件
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'DoubanSpider.middlewares.DoubanspiderDownloaderMiddleware': 543,
#}

# 启用或禁用扩展程序
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# 配置项目管道
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'DoubanSpider.pipelines.DoubanspiderPipeline': 300,
}

# 启用或禁用AutoThrottle扩展程序(默认关闭)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# 初始下载延迟
#AUTOTHROTTLE_START_DELAY = 5
# 设置最大下载延迟
#AUTOTHROTTLE_MAX_DELAY = 60
