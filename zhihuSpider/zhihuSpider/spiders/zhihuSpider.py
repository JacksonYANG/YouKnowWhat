import re
import scrapy
from bs4 import BeautifulSoup
from scrapy.http import Request
from zhihuSpider.zhihuSpider.items import zhihuSpiderItem
import codecs

class zhihuSpider(scrapy.Spider):
    name = 'zhihuSpider'
    allowed_domains = ['zhihu.com']

    ##开始爬虫请求
    def start_requests(self):
        url = 'https://www.zhihu.com/signin'
        yield Request(url,self.parse())

    ##解析
    def parse(self, response):
        print(response.body)