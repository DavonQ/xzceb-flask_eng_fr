import unittest
from translator import Translator

class TranslatorTests(unittest.TestCase):

    def setUp(self):
        self.translator = Translator()

    def test_englishToFrench_hello(self):
        english_text = 'Hello'
        expected_french_text = 'Bonjour'
        result = self.translator.english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_englishToFrench_bonjour(self):
        english_text = 'Bonjour'
        expected_french_text = 'Bonjour'  # Since 'Bonjour' is already a French word
        result = self.translator.english_to_french(english_text)
        self.assertEqual(result, expected_french_text)

    def test_frenchToEnglish_bonjour(self):
        french_text = 'Bonjour'
        expected_english_text = 'Hello'
        result = self.translator.french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

    def test_frenchToEnglish_hello(self):
        french_text = 'Hello'  # Since 'Hello' is the same in English
        expected_english_text = 'Hello'
        result = self.translator.french_to_english(french_text)
        self.assertEqual(result, expected_english_text)

if __name__ == '__main__':
    unittest.main()
