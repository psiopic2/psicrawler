import scrapy
from scrapy.spiders import Rule
from scrapy.linkextractors import LinkExtractor
from newspaper import Article, Config
from psicrawler.spiders.default_spider import DefaultSpider
import os
# archive lists
# https://en.wikinews.org/wiki/Wikinews:[year]/[month]/[date]

class WikinewsEnSpider(DefaultSpider):
    name = "wikinews_en"
    source = "wikinews-en"
    allowed_domains = ["en.wikinews.org"]
    start_urls = [
        "https://en.wikinews.org/wiki/Wikinews:Archives/Date/All"
    ]

    rules = (
        Rule(LinkExtractor(allow=('Wikinews\:[0-9][0-9][0-9][0-9]\/[A-Za-z]+\/[0-9]+'), deny=('\/w\/index.php'))),
        Rule(LinkExtractor(allow=('wiki\/*'), deny=(
            'Wikinews\:*', 
            'Special\:*', 
            'Category\:*',
            'Wikinoticias\:*',
            'User\:*',
            'User_talk\:*',
            '\/w\/index\.php*'
        )), callback='parse_article'),
    )

    source = "wikinews-en"

    mapped_topics = {
        'Politics and conflicts': 'Politics',
        'Disasters and accidents': 'Disasters',
        'Economy and business': 'Economics',
        'Culture and entertainment': 'Entertainment',
        'Science and technology': 'Science',
        'Weather': 'Environment',
        'Internet': 'Science',
        'Crime and law': 'Law',
    }

    # allowed_topics = None
        

    def extract_title(self, title):
        t = super().extract_title(title)
        return t.replace(' - Wikinews, the free news source', '')

    def extract_text(self, response):
        a = super().extract_text(response)
        a = a.replace('From Wikinews, the free news source you can write!','')
        a = a.replace('This page is archived, and is no longer publicly editable. Articles presented on Wikinews reflect the specific time at which they were written and published, and do not attempt to encompass events or knowledge which occur or become known after their publication. Got a correction? Add the template {{editprotected}} to the talk page along with your corrections, and it will be brought to the attention of the administrators. Please note that due to our archival policy, we will not alter or update the content of articles that are archived, but will only accept requests to make grammatical and formatting corrections. Note that some listed sources or external links may no longer be available online due to age.','')

        return a

    def extract_topics(self, response):
        topics = response.xpath('//div[@id="mw-normal-catlinks"]/ul/li/a/text()').extract()
        return self.filter_topics(topics)

