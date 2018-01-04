##coding=utf-8

###这是一个爬虫脚本，用于爬取知乎对应问题的相应答案,使用requests+scrapy库的结合

import requests
import scrapy
import re
from bs4 import BeautifulSoup
import codecs


