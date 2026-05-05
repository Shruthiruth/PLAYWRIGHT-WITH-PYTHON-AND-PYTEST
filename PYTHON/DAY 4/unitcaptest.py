import unittest
import capunittest

class TestCapText(unittest.TestCase):
    def test_cap_text(self):
        text = "hello"
        result = capunittest.cap_text(text)
        self.assertEqual(result, "Hello")
        
    def test_cap_text_empty(self):
        text = ""
        result = capunittest.cap_text(text)
        self.assertEqual(result, "")
        
    def test_cap_multiple_words(self):
        text = "hello world"
        result = capunittest.cap_text(text)
        self.assertEqual(result, "Hello world")
        
if __name__ == '__main__':
    unittest.main()
        