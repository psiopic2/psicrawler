"""
Crawl job for Australian Broadcast Corporation Archives

http://www.abc.net.au/news/archive
"""
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from psicrawler.spiders.default_spider import DefaultSpider

class AustralianBroadcastCorpArchivesSpider(DefaultSpider):

    name = "australian_broadcast_corp_archives"
    allowed_domains = ["www.abc.net.au"]
    start_urls = [
            "http://www.abc.net.au/news/archive/"
    ]

    rules = (
        Rule(LinkExtractor(allow=('/archive/[0-9]+','/archive/[0-9]+,[0-9]+','/archive/[0-9]+,[0-9]+,[0-9]+'))),
        Rule(LinkExtractor(allow=('/news/[0-9]+\-[0-9]+\-[0-9]+/*')), callback='parse_article')
    )

    source = "australian-broadcast-corp-archives"

    mapped_topics = {
        'World Politics': 'Politics',
        'Business, Economics and Finance': 'Economics',
        'Government and Politics': 'Politics',
        'Unrest, Conflict and War': 'Politics',
        'Disasters and Accidents': 'Disasters',
        'Arts and Entertainment': 'Entertainment',
        'Law, Crime and Justice': 'Law',
        'Courts and Trials': 'Law',
        'Science and Technology': 'Science',
        'Banking': 'Economics',
        'Industry': 'Economics',
        'Lifestyle and Leisure': 'Entertainment',
        'Crime': 'Law',
        'police': 'Law'
    }

    # allowed_topics = None

    def extract_topics(self, response):
        return self.filter_topics(response.xpath('//meta[@property="article:tag"]/@content').extract())

