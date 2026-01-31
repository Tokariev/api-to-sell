import unittest

from utils.HtmlCharacterDecoder import HtmlCharacterDecoder


class TestsHtmCharacterDecoder(unittest.TestCase):

    def setUp(self):
        self.htmlCharacterDecoder = HtmlCharacterDecoder()

    def test_escape(self):
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&#39;'), "'")
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&#x2F;'), "/")
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('test&#x2F;'), "test/")
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&quot;'), '"')
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&gt;'), '>')
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&lt;'), '<')
        self.assertEqual(self.htmlCharacterDecoder.escape_html_codes('&amp;'), '&')

