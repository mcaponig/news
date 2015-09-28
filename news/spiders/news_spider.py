# -*- coding: utf-8 -*-

'''NewsItem is Item object with 8 fields:
    title: article title
    url: canonical url
    desc: desription of article, usually taken from meta tag
    author: article author when available
    datetime: default search is date published, may need to formatting to be interpretted as date
    arttype: Field to determine type of website
    site: Field to contain data for Site name
    text: Field for text which references "Notre Dame"
'''
import scrapy
import sys
sys.path.append('/Users/matthewcaponigro/Documents/Analytics-Code/news/news')

from news.items import NewsItem
from descriptioncheck import description
from authorcheck import authorname
from articlecheck import article
from sitename import sitename
from datecheck import datecheck
from urlcheck import urlcheck
from titlecheck import titlecheck
from sourcecheck import sourcecheck

# import sys
# sys.path.append('/Users/matthewcaponigro/Documents/Analytics/news/news') # this path address will need refactored if script is moved
class NewsSpider(scrapy.Spider):
    name = "newsgen"
    allowed_domains = ['*']
    start_urls = (
    'http://www.washingtontimes.com/news/2015/sep/21/sierra-club-notre-dames-plan-to-cut-coal-use-good-/',
    'http://www.huffingtonpost.com/entry/colombian-president-rebels-reach-breakthrough-in-talks_56033377e4b0fde8b0d1379e'
    )

    def parse(self, response):
        item = NewsItem()
        htmg = response.xpath('//html').extract()
        html = htmg[0]

        # Run through basic checker for relevance
        if "Notre Dame" in html:
            item['title'] = titlecheck(response,html)
            item['url'] = urlcheck(response,html)
            item['desc'] = description(response,html)
            item['author'] = authorname(response,html)
            item['datetime'] = datecheck(response,html)
            item['arttype'] = article(response,html)
            item['source'] = sourcecheck(response,html)
            item['site'] = sitename(response,html)
            item['text'] = response.xpath('//*[text()[contains(.,"Notre Dame")]]/text()').extract()
            yield item
        else:
            pass