# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from quotetutorial.items import QuotetutorialItem
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')

class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        quotes = response.css('.quote')#class = quote
        for quote in quotes:
            item = QuotetutorialItem()
            text = quote.css('.text::text').extract_first()#class = text
            author = quote.css('.author::text').extract_first()
            tags = quote.css('.tag::text').extract()#find  findall
            item['quotes'] = text
            item['author'] = author
            item['tags'] = tags
            yield item

        # next = response.css('.pager .next a::attr(href)').extract_first()
        # url = response.urljoin(next)
        # yield scrapy.Request(url=url, callback=self.parse)

