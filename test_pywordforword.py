import unittest
import os
from PyWordforWord import PyWordForWord

class TestPyWordForWord(unittest.TestCase):

    def setUp(self):
        self.pww = PyWordForWord()
        self.test_dir = '/Users/peter/Dev/PyWordForWord/testdata'
        self.single_file = os.path.join(self.test_dir, 'testdata2.txt')
        self.single_content = (
            "We the People of the United States, in Order to form a more perfect Union, "
            "establish Justice, insure domestic Tranquility, provide for the common defence, "
            "promote the general Welfare, and secure the Blessings of Liberty to ourselves "
            "and our Posterity, do ordain and establish this Constitution for the United States of America."
        ).replace("\n", " ")

    def test_print(self):
        content = self.pww.print(self.single_file).replace("\n", " ")
        self.assertEqual(content.strip(), self.single_content.strip())

    def test_wc(self):
        content = self.pww.print(self.single_file)
        num_lines, num_words, num_chars = self.pww.wc(content)
        self.assertEqual(num_lines, 4)  # Update to reflect the actual number of lines
        self.assertEqual(num_words, 52)
        self.assertEqual(num_chars, len(content))

    def test_wordFrequency(self):
        content = self.pww.print(self.single_file)
        word_freq = self.pww.wordFrequency(content)
        self.assertEqual(word_freq['the'], 2)
        self.assertEqual(word_freq['and'], 1)

    def test_letterFrequency(self):
        content = self.pww.print(self.single_file)
        letter_freq = self.pww.letterFrequency(content)
        self.assertEqual(letter_freq['e'], 38)
        self.assertEqual(letter_freq['t'], 26)

    def test_frequency(self):
        content = self.pww.print(self.single_file)
        self.pww.wordFrequency(content)
        freq = self.pww.frequency('the')
        self.assertAlmostEqual(freq, 2/52)

    def test_process_file(self):
        result_file = self.pww.process_file(self.single_file)
        self.assertTrue(os.path.isfile(result_file))

    def test_process_directory(self):
        result_file = self.pww.process_directory(self.test_dir)
        self.assertTrue(os.path.isfile(result_file))

if __name__ == "__main__":
    unittest.main()
