'''arttype.py 
for use checking article type marker in html markup
implemented in 'news.py' Scrapy spider
Last updated 9/26/2015
'''

def article(response,html):
	if 'property="og:type"' in html:
		return response.xpath('//meta[@property="og:type"]/@content').extract()
	elif 'class="article-type"' in html:
		return response.xpath('//span[@class="article-type"]/text()').extract()
	elif 'rel="search"' in html:
		return response.xpath('//link[@rel="search"/@title').extract()
	elif 'property="contenttype"' in html:
		return response.xpath('//meta[@property="contenttype"/@content').extract()
	else:
		return "NULL"
		