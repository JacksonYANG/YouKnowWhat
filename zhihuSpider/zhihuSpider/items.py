# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class zhihuSpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    #答案
    answer = scrapy.Field()

    #对应详细答案的URL
    answer_url = scrapy.Field()
