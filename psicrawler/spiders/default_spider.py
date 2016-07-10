from scrapy.spiders import CrawlSpider
from psicrawler.items import GenericItem
from newspaper import Article, Config as ArticleConfig
import os

class DefaultSpider(CrawlSpider):

    source = "DefaultSpider"

    allowed_topics = (
        'Technology',
        'Economics',
        'Politics',
        'Science',
        'Disasters',
        'Health',
        'Sports',
        'Entertainment',
        'Environment',
        'Law'
    )

    mapped_topics = {}

    def extract_url(self, response):
        return response.url

    def extract_title(self, response):
        return response.xpath('//title/text()').extract()[0]

    def extract_text(self, response):

        conf = ArticleConfig()
        conf.fetch_images = False
        conf.follow_meta_refresh = False
        conf.memoize_articles = False

        article = Article(url=response.url, config=conf)
        article.download(html=response.body)
        article.parse()

        return article.text

    def filter_topics(self, topics):
        newtopics = []
        for topic in topics:
            if topic in self.mapped_topics:
                topic = self.mapped_topics[topic]

            if self.allowed_topics == None or topic in self.allowed_topics:
                newtopics.append(topic)
                
        return newtopics


    def extract_topics(self, response):
        return ()

    def parse_article(self, response):
        i = GenericItem()
        i['text'] = self.extract_text(response)
        i['topics'] = self.extract_topics(response)
        i['title'] = self.extract_title(response)
        i['url'] = self.extract_url(response)
        i['source'] = self.source

        # self.write_item(i)
        return i
