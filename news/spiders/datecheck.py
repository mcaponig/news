'''datecheck.py 
checks html tag for date published
for use with Scrapy spider "new.py"
Last update: 9/26/2015
'''

def datecheck(response,html):
	if 'name="utime"' in html:
		return resposne.xpath('//meta[@name="utime"/@content').extract()
	elif 'name="date"' in html:
		return response.xpath('//meta[@name="date"]/@content').extract()
	elif 'name="dat"' in html:
		return response.xpath('//meta[@name="dat"]/@content').extract()
	elif 'class="date-created"' in html:
		return response.xpath('//meta[@class="date-created"]/text()').extract()
	elif 'span itemprop="datePublished"' in html:
		return response.xpath('//span[@itemprop="datePublished"]/text()').extract()
	elif 'meta itemprop="datePublished"' in html:
		return response.xpath('//meta[@itemprop="datePublished"]/@content').extract()
	elif 'class="entry-date published"' in html:
		return response.xpath('//meta[@class="entry-date published"]/text()').extract()
	elif 'class="toLocalTime"' in html:
		return response.xpath('//meta[@class="toLocalTime"]/@data-tlt-epoch-time)').extract()
	elif 'datatype="xsd:dateTime"' in html:
		return response.xpath('//meta[@datatype="xsd:dateTime"]/@content').extract()
	elif 'class="asset-metabar-time asset-metabar-item nobyline"' in html:
		return response.xpath('//meta[@class="asset-metabar-time asset-metabar-item nobyline"]/text()').extract()
	elif 'class="time"' in html:
		return response.xpath('//span[@class="time"]/text()').extract()
	elif 'name="pubdate"' in html:
		return response.xpath('//meta[@name="pubdate"]/text()').extract()
	elif 'class="dateline"' in html:
		return response.xpath('//p[@class="dateline"]/text()').extract()
	elif 'name="article.published"' in html:
		return response.xpath('//meta[@name="article.published"]/@content').extract()
	elif 'class="created"' in html:
		return response.xpath('//time[@class="created"]/text()').extract()
	else:
		return ["NULL"]