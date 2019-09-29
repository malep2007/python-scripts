import unittest
from main import compress_list

class ListComprehensionTestCase(unittest.TestCase):
    def setUp(self):
        self.input_list = [2,1,2,3,4,5,6]
        self.empty_list = [1,2,3,4,5,6]
        self.wrong_type = 43

    def test_returns_correct_value(self):
        self.assertEqual(compress_list(self.input_list), [2,2,4,6])
    
    def test_returns_empty_list(self):
        self.assertEqual(compress_list(self.empty_list), [])
    
    def test_does_not_compute_wrong_input(self):
        self.assertRaises(TypeError, compress_list(self.wrong_type))

if __name__ == "__main__":
    import unittest.main
