# logical test for author attribute
def authorname(response,html):
	if 'name="Author"' in html: #General Meta tag
		return response.xpath('//meta[@name="Author"]/@content').extract()
	elif 'name="author"' in html:
		return response.xpath('//meta[@name="author"]/@content').extract()
	elif 'class="AuthorName"' in html:	# Washington Post markup
		return response.xpath('//span[@class="AuthorName"]/text()').extrct()
	elif 'name="author"' in html:		#NYTimes article
		return response.xpath('//meta[@name="author"]/@content').extract()
	elif 'class="authorName"' in html:	#indepent.uk.co 
		return response.xpath('//a/span[@class="authorName"]/text()').extract
	elif 'class="name fn"' in html: 	#Huffington Post
		return response.xpath('//span[@class="name fn"]/text()').extract()
	elif 'class="fn"' in html: 	#Nature
		return response.xpath('//a[@class="fn"]/text()').extract()
	elif 'itemprop="name"' in html:
		return response.xpath('//span[@itemprop="name"]/text()').extract()
	else:
		return ["NULL"]
