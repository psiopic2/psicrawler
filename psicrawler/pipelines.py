# -*- coding: utf-8 -*-
import os

class PsicrawlerPipeline(object):
    
    def get_base_path(self):
        return os.path.dirname(os.path.realpath(__file__)) + "/../xmlfiles"
    
    def write_item(self, item):

        if len(item['topics']) > 0:
            targetDir = self.get_base_path()

            firstLetter = item['title'][0].lower()
            targetDir += '/' + firstLetter

            if os.path.exists(targetDir) == False:
                os.makedirs(targetDir)

            fn = item['title'].replace(' ', '_') + '.xml'

            with open(targetDir + '/' + fn, 'w') as f:
                f.write(item.asXml())    
    
    def process_item(self, item, spider):
        self.write_item(item)
        return item
