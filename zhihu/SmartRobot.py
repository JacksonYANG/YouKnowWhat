##coding=utf-8

###这是一个爬虫脚本，用于爬取知乎对应问题的相应答案,使用requests+scrapy库的结合
###通过分析知乎搜索URL可以得出，知乎URL的链接是

import requests
import scrapy
import re
from bs4 import BeautifulSoup
import codecs

class zhihuSpider(scrapy.Spider):
    name = 'smartzhihu'
    allowed_domains = ['zhihu.com']
    start_urls = [
        'https://www.zhihu.com/'
    ]

    def parse(self, response):
        filename = response.url.split('/')[-2]
        with open(filename,'w+') as f:
            f.write(response.body)


