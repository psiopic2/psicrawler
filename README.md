# psicrawler

This tool will crawl various news websites, extract article data, the article's topics or tags, and create an XML-based corpus

## Requirements

python v3 is required to run this tool

## Installation

```
$ git clone https://github.com/psiopic2/psicrawler.git
$ cd psicrawler
$ virtualenv -p python3 env
$ source env/bin/activate
$ pip install -r requirements/psicrawler.txt
```

## Available crawl jobs

1. wikinews-en
2. telegraph-archives

## Start a job

```
$ scrapy crawl wikinews-en
```

## Output

Files are stored in the directory xmlfiles.

Each XML looks like so:

```xml
<?xml version="1.0" encoding="utf-8"?>
<document>
  <title></title>
  <topics>
    <topic></topic>
    ...
    <topic></topic>
  </topics>
  <url></url>
  <source></source>
  <text><?[CDATA[ ]]></text>
</document>
```

## Tools

### analyze.py

This tool can tell you some statistics about your xml corpus.

```
$ ./analyze.py --stats
```

Lists various statistical information about the corpus

```
$ ./analyze.py --stats --source=wikinews-en
```

Lists the same statistics, but only for a specific source/crawl job

```
$ ./analyze.py --topic=Disasters
```

Lists URLs that are associated with the topic Disasters

