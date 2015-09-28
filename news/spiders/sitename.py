'''sitename.py 
checks if sitename tag present for website scraped
for use with Scrapy spider "new.py"
Last udpated: 9/26/2015
'''

def sitename(response,html):
	if 'property="og:site_name"' in html:
		return response.xpath('//meta[@property="og:site_name"]/@content').extract()
	elif 'name="cre"' in html:
		return response.xpath('//meta[@name="cre"]/@content').extract()
	elif 'class="copyright"' in html:
		return response.xpath('//meta[@class="copyright"]/text()').extract()
	elif 'rel="index"' in html:
		return response.xpath('//link[@rel="index"]/@title').extract()
	else:
		return "NULL"
