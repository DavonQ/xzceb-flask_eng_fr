from deep_translator import MyMemoryTranslator

class Translator:
    def __init__(self):
        self.translator = MyMemoryTranslator()

    def english_to_french(self, english_text):
        """
        Translates English text to French.

        Args:
            english_text (str): The English text to translate.

        Returns:
            str: The translated French text, or an error message if translation fails.
        """
        try:
            if not isinstance(english_text, str) or not english_text.strip():
                raise ValueError("Invalid input: English text must be a non-empty string")

            french_text = self.translator.translate(english_text, source='en', target='fr')
            return french_text
        except Exception as e:
            return f"Translation error: {str(e)}"

    def french_to_english(self, french_text):
        """
        Translates French text to English.

        Args:
            french_text (str): The French text to translate.

        Returns:
            str: The translated English text, or an error message if translation fails.
        """
        try:
            if not isinstance(french_text, str) or not french_text.strip():
                raise ValueError("Invalid input: French text must be a non-empty string")

            english_text = self.translator.translate(french_text, source='fr', target='en')
            return english_text
        except Exception as e:
            return f"Translation error: {str(e)}"
