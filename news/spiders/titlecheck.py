'''titlecheck.py
last update: 9/26/2015
'''

def titlecheck(response,html):
	if "og:title" in html:
		return response.xpath('//meta[@property="og:title"]/@content').extract()
	elif "title" in html:
		return response.xpath('//title/text()').extract()
	else:
		return "NULL"
		
