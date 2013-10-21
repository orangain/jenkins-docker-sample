# coding: utf-8

import unittest

from lxml import etree

class TestXML(unittest.TestCase):

    def test_xpath(self):
        root = etree.XML("""
            <root>
                <person>
                    <name>山田</name>
                    <age>15</age>
                </person>
                <person>
                    <name>佐藤</name>
                    <age>43</age>
                </person>
            </root>
            """)

        self.assertEqual(root.xpath('//person/name/text()'), ['山田', '佐藤'])
