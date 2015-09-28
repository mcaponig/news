'''sourcecheck.py
checks if source tag for article
Last updated: 9/27/2015
'''

def sourcecheck(response,html):
	if 'class="source"' in html:
		return response.xpath('//span[@class="source"]/text()').extract()
	if "The Associated Press" in html:
		return ["Associated Press"]
	else:
		return "NULL"