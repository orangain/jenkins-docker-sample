# coding: utf-8

from lxml import etree

class ConfigReader(object):

    def __init__(self, xml_string):
        self.root = etree.XML(xml_string)

    def get_names(self):
        return self.root.xpath('//person/name/text()')

    def get_ages(self):
        return self.root.xpath('//person/age/text()')
