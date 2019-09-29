from unittest import TestCase
from recurring_string import repeated_character

class TestRecurringString(TestCase):
    def test_returns_correct_answer(self):
        self.assertEqual('r', repeated_character('overrated'))
        self.assertEqual('B', repeated_character("ABCDBA"))

    
