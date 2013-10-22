# coding: utf-8

import unittest

from config_reader import ConfigReader

class TestConfigReader(unittest.TestCase):

    def setUp(self):
        self.config = ConfigReader("""
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


    def test_get_names(self):
        self.assertEqual(self.config.get_names(), ['山田', '佐藤'])

    def test_get_ages(self):
        self.assertEqual(self.config.get_ages(), ['15', '43'])
