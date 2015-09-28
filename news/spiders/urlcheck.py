'''urlcheck.py
for use with Scrapy spider "news.py"
last updated: 9/26/2015
'''

def urlcheck(response,html):
	if 'property="og:url"' in html:
		return response.xpath('//meta[@property="og:url"]/@content').extract()
	elif 'rel="canonical"' in html:
		return response.xpath('//link[@rel="canonical"/@href').extract()
	else:
		return "NULL"