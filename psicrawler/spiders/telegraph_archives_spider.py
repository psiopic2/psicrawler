import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from newspaper import Article, Config
from psicrawler.spiders.default_spider import DefaultSpider
import os
# archive lists
# https://en.wikinews.org/wiki/Wikinews:[year]/[month]/[date]

class TelegraphArchivesSpider(DefaultSpider):

    name = "telegraph_archives"
    allowed_domains = ["www.telegraph.co.uk"]
    start_urls = [
            "http://www.telegraph.co.uk/archive"
    ]

    rules = (
        Rule(LinkExtractor(allow=('/archive/[0-9]+\.html','/archive/[0-9]+\-[0-9]+\.html','/archive/[0-9]+\-[0-9]+\-[0-9]+\.html'))),
        Rule(LinkExtractor(allow=('/news/*.html')), callback='parse_article'),
        Rule(LinkExtractor(allow=('/news/*')), callback='parse_article')
    )

    source = "telegraph-archives"

    mapped_topics = {
        'Technology and News': 'Technology',
        'Business Latest News': 'Economics',
        'Finance': 'Economics',
        'Banks and Finance': 'Economics',
        'Retail and Consumer': 'Economics',
        'Industry': 'Economics',
        'Celebrity news': 'Entertainment',
        'Law and Order': 'Law',
        'Earth News': 'Environment',
        'Crime': 'Law',
        'Technology News': 'Technology',
        'Construction and Property': 'Economics',
        'Health News': 'Health',
        'Science News': 'Science'
    }

    # allowed_topics = None

    def extract_topics(self, response):
        return self.filter_topics(response.xpath('//meta[@property="article:tag"]/@content').extract())

