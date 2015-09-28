#tests types of 'type' meta tags for repsonse
def type(response,html):	
	if 'property="og:type"' in html: #HuffPo
		return response.xpath('//meta[@property="og:type"]/@content').extract()
	elif 'itemprop="genre"' in html: #NYT
		return response.xpath('//meta[@itemprop="genre"/@content').extract()
	elif 'meta property="og:type"' in html: #WashPost
		return response.xpath('//meta[@property="og:type"]/@content').extract()
	else:
		return "NULL"
		