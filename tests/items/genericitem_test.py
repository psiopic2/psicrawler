from psicrawler.items import GenericItem
from psicrawler.items import from_xml

def test_xml_generation_with_topics():
    
    expected_xml = """<?xml version="1.0" encoding="utf-8"?>
<document>
  <title>Foobar</title>
  <url>http://foobar</url>
  <topics>
    <topic>Topic 1</topic>
    <topic>Topic 2</topic>
  </topics>
  <source>foobar</source>
  <text><![CDATA[wharblegarble]]></text>
</document>"""

    
    i = GenericItem()
    i['title'] = 'Foobar'
    i['url'] = 'http://foobar'
    i['source'] = 'foobar'
    i['topics'] = ('Topic 1', 'Topic 2')
    i['text'] = 'wharblegarble'
    
    assert i.asXml() == expected_xml
    
def test_xml_generation_without_topics():
    expected_xml = """<?xml version="1.0" encoding="utf-8"?>
<document>
  <title>Foobar</title>
  <url>http://foobar</url>
  <topics>
  </topics>
  <source>foobar</source>
  <text><![CDATA[wharblegarble]]></text>
</document>"""

    
    i = GenericItem()
    i['title'] = 'Foobar'
    i['url'] = 'http://foobar'
    i['source'] = 'foobar'
    i['topics'] = ()
    i['text'] = 'wharblegarble'
    
    assert i.asXml() == expected_xml 
    
def test_item_from_xml_with_topics(tmpdir):

    xml = """<?xml version="1.0" encoding="utf-8"?>
<document>
  <title>Foobar</title>
  <url>http://foobar</url>
  <topics>
    <topic>Topic 1</topic>
    <topic>Topic 2</topic>
  </topics>
  <source>foobar</source>
  <text><![CDATA[wharblegarble]]></text>
</document>"""

    p = tmpdir.mkdir('fixtures').join('itemxml.xml')
    p.write(xml)
    
    i = from_xml(str(p))
    assert i['title'] == 'Foobar'
    assert i['url'] == 'http://foobar'
    assert i['source'] == 'foobar'
    assert i['text'] == 'wharblegarble'
    assert i['topics'][0] == 'Topic 1'
    assert i['topics'][1] == 'Topic 2'
    
def test_item_from_xml_without_topics(tmpdir):

    xml = """<?xml version="1.0" encoding="utf-8"?>
<document>
  <title>Foobar</title>
  <url>http://foobar</url>
  <topics>
  </topics>
  <source>foobar</source>
  <text><![CDATA[wharblegarble]]></text>
</document>"""

    p = tmpdir.mkdir('fixtures').join('itemxml.xml')
    p.write(xml)
    
    i = from_xml(str(p))
    assert i['title'] == 'Foobar'
    assert i['url'] == 'http://foobar'
    assert i['source'] == 'foobar'
    assert i['text'] == 'wharblegarble'
    assert i['topics'] == ()

