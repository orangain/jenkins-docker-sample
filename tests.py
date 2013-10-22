# coding: utf-8

import unittest

from config_reader import ConfigReader

class TestConfigReader(unittest.TestCase):

    def test_get_names(self):
        config = ConfigReader("""
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

        self.assertEqual(config.get_names(), ['山田', '佐藤'])
