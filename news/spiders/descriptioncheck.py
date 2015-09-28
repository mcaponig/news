'''description check
for use with news.py spider in Scrapy library
'''

def description(response,html):
	if 'name="decription"'in html:
		return response.xpath('//meta[@name="description"]/@content').extract()
	elif 'property="og:description"'in html:
		return response.xpath('//meta[@property="og:description"]/@content').extract()
	else:
		return "NULL"