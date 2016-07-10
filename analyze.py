#!/usr/bin/env python
"""Psicrawler Analzyer

Usage:
    analyze.py [--xmlfiles=<dir>] [--source=<source>] [--topic=<topic>] [--stats]

Options:
    --xmlfiles=<dir>    Location of xml files prepared by crawl jobs
    --source=<source>   Filter on a specific source
    --topic=<topic>     Show URLs for a specific topic
    --stats             Show statistics of the corpus

"""
from docopt import docopt
import os
import operator
import xml.etree.ElementTree
from psicrawler.items import from_xml

def gather_topic_count(e):

    topics = {}

    for topic in e.iter('topic'):
        t = topic.text
        if t not in topics:
            topics[t] = 1
        else:
            topics[t] += 1

    return topics

def gather_source(e):
    return e.findall('source')[0].text


def show_topic_urls(conf):

    urls = []

    for root, subdirs, files in os.walk(conf['xmlfiles']):
        for filename in files:
            fn = os.path.join(root, filename)
            item = from_xml(fn)

            if conf['source'] == None or conf['source'] == item['source']:
                if conf['topic'] in item['topics']:
                    urls.append(item['url'])

    print('---- URLS FOR TOPIC: "%s" ----' % conf['topic'])
    for url in urls:
        print(url)

def show_statistics(conf):

    topics = {}
    sources = {}

    total_files = 0

    filterSource = conf['source']


    for root, subdirs, files in os.walk(conf['xmlfiles']):
        for filename in files:
            fn = os.path.join(root, filename)
            item = from_xml(fn)

            if filterSource != None and filterSource != item['source']:
                continue

            for topic in item['topics']:
                if topic not in topics:
                    topics[topic] = 1
                else:
                    topics[topic] += 1

            if item['source'] not in sources:
                sources[item['source']] = 1
            else:
                sources[item['source']] += 1


            total_files += 1


    print("---- TOP 40 TOPICS ----")
    sorted_x = sorted(topics.items(), key=operator.itemgetter(1), reverse=True)
    for x in sorted_x[0:40]:
        topic,count = x
        print('%-30s: %s' % (topic, count))
    
    print("---- SOURCES ----")
    sorted_x = sorted(sources.items(), key=operator.itemgetter(1), reverse=True)
    if len(sorted_x) > 0:
        for source, count in sorted_x:
            print('%-30s: %s' % (source, count))

    print("---- STATISTICS ----")
    print('%-30s: %s' % ('Total File Count:', total_files))

if __name__ == '__main__':
    arguments = docopt(__doc__, version='0.0.1')

    conf = {
        'xmlfiles': arguments['--xmlfiles'],
        'stats': arguments['--stats'],
        'source': arguments['--source'],
        'topic': arguments['--topic']
    }

    if conf['xmlfiles'] == None:
        conf['xmlfiles'] = './xmlfiles'

    if conf['topic'] != None:
        show_topic_urls(conf)

    if conf['stats'] == True:
        show_statistics(conf)

    # iterate_files(xmlfiles, arguments)

