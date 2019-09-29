import unittest
from main import compound_words

class EnglishWordTestCase(unittest.TestCase):
    def setUp(self):
        self.input_sequence = ['paris', 'applewatch', 'ipod', 'amsterdam', 'bigbook', 'orange', 'waterbottle']

    def test_gives_correct_output(self):
        self.assertEqual(compound_words(self.input_sequence), ['applewatch', 'bigbook', 'waterbottle']) 


if __name__ == "__main__":
    import unittest.main
