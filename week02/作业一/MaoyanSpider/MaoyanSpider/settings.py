# -*- coding: utf-8 -*-

# Scrapy settings for MaoyanSpider project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'MaoyanSpider'

SPIDER_MODULES = ['MaoyanSpider.spiders']
NEWSPIDER_MODULE = 'MaoyanSpider.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'MaoyanSpider (+http://www.yourdomain.com)'

# Obey robots.txt rules
ROBOTSTXT_OBEY = True

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
  'Accept-Language': 'en',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36',
  'Cookie': 'uuid_n_v=v1; uuid=39FC6F70B85411EAA94453F28D7995DF30374A1B311048A9B8C0900DBC5F4AFA; _csrf=e6b5b20adff4d4b71bf4303351c7d78324a1cf5dc7d7c26de74a65faab1d5b13; mojo-uuid=fbe505445402c37757b6d1cf54e300ff; _lxsdk_cuid=172f4ff1214c8-0cd354d6e5c9a9-3b634504-1fa400-172f4ff1214c8; _lxsdk=39FC6F70B85411EAA94453F28D7995DF30374A1B311048A9B8C0900DBC5F4AFA; Hm_lvt_703e94591e87be68cc8da0da7cbd0be2=1593248257,1593248489; Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2=1593258659; __mta=108402749.1593248261085.1593255186016.1593258662548.9; _lxsdk_s=172f5d6acb8-204-e6c-4d5%7C%7C1'
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'MaoyanSpider.middlewares.MaoyanspiderSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   'MaoyanSpider.middlewares.MaoyanspiderDownloaderMiddleware': 543,
   'MaoyanSpider.middlewares.RandomHttpProxyMiddleware': 400,
}
HTTP_PROXY_LIST=[
    'http://52.179.231.206:80',
    'http://95.0.194.241:9090',
]

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'MaoyanSpider.pipelines.MaoyanspiderPipeline': 300,
   'MaoyanSpider.pipelines.SavetoMySQLPipeline': 300,
}
#settings for mysql
MYSQL_SERVER = "127.0.0.1"
MYSQL_DB     = "test"
MYSQL_TABLE  = "movies" # the table will be created automatically
MYSQL_USER   = "test"        # MySQL user to use (should have INSERT access granted to the Database/Table
MYSQL_PWD    = "test"        # MySQL user's password

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
