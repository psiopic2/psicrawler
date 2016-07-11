"""
Crawl job for CNN

http://edition.cnn.com
"""
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from psicrawler.spiders.default_spider import DefaultSpider

class NationalPostSpider(DefaultSpider):

    name = "national_post"
    allowed_domains = ["news.nationalpost.com"]
    start_urls = [
            "http://news.nationalpost.com/2001",
            "http://news.nationalpost.com/2002",
            "http://news.nationalpost.com/2003",
            "http://news.nationalpost.com/2004",
            "http://news.nationalpost.com/2005",
            "http://news.nationalpost.com/2006",
            "http://news.nationalpost.com/2007",
            "http://news.nationalpost.com/2008",
            "http://news.nationalpost.com/2009",
            "http://news.nationalpost.com/2010",
            "http://news.nationalpost.com/2011",
            "http://news.nationalpost.com/2012",
            "http://news.nationalpost.com/2013",
            "http://news.nationalpost.com/2014",
            "http://news.nationalpost.com/2015",
            "http://news.nationalpost.com/2016"
    ]

    rules = (
        Rule(LinkExtractor(allow=('[0-9]+/page/[0-9]+'))),
        Rule(LinkExtractor(allow=('/sports', '/news','/holy-post','/arts','/posted-toronto')), callback='parse_article')
    )

    source = "national-post"

    mapped_topics = {
        'sports': 'Sports',
        'business': 'Economics',
        'politics': 'Politics',
        'finance': 'Economics',
        'entertainment': 'Entertainment',
        'financial news': 'Economics',
        'canadian politics': 'Politics',
        'music': 'Entertainment',
        'world politics': 'Politics',
        'u.s. politics': 'Politics',
        'movies': 'Entertainment',
        'crime': 'Law',
    }

    # allowed_topics = None

    def extract_topics(self, response):
        
        # section = response.xpath('//meta[@name="section"]/@content').extract()[0]
        keywords = response.xpath('//meta[@name="keywords"]/@content').extract()[0].split(',')
        
        topics = []
        for k in keywords:
            topics.append(k.strip())
        
        return self.filter_topics(topics)

