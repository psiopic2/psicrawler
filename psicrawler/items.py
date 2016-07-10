# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from xml.sax.saxutils import escape
import xml.etree.ElementTree

def from_xml(xmlfile):
    e = xml.etree.ElementTree.parse(xmlfile).getroot()

    topics = []
    for topic in e.iter('topic'):
        topics.append(topic.text)

    title = e.findall('title')[0].text
    url = e.findall('url')[0].text
    source = e.findall('source')[0].text
    text = e.findall('text')[0].text

    i = GenericItem()
    i['title'] = title
    i['topics'] = topics
    i['source'] = source
    i['url'] = url
    i['text'] = text

    return i



class GenericItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    text = scrapy.Field()
    topics = scrapy.Field()
    title = scrapy.Field()
    url = scrapy.Field()
    source = scrapy.Field()

    def asXml(self):

        xmlstr = '<?xml version="1.0" encoding="utf-8"?>\n'
        xmlstr += '<document>\n'
        xmlstr += '  <title>%s</title>\n' % escape(self['title'])
        xmlstr += '  <url>%s</url>\n' % escape(self['url'])
        
        xmlstr += '  <topics>\n'
        for topic in self['topics']:
            xmlstr += '    <topic>' + escape(topic) + '</topic>\n'
        xmlstr += '  </topics>\n'
        xmlstr += '  <source>' + escape(self['source']) + '</source>\n'
        xmlstr += '  <text><![CDATA[' + self['text'] + ']]></text>\n'
        xmlstr += '</document>'

        return xmlstr
