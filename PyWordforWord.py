import os
import re
from collections import Counter
from typing import Tuple, Dict

class PyWordForWord:
    def __init__(self):
        self.total_words = 0
        self.word_freq = Counter()

    def print(self, filename: str) -> str:
        """
        Reads the contents of a file, line by line, and creates a String object,
        preserving all the newlines.
        """
        with open(filename, 'r') as file:
            content = file.read()
        return content

    def wc(self, input_text: str) -> Tuple[int, int, int]:
        """
        Counts the number of characters, words, and lines in the input text.
        Returns a tuple with the number of lines, words, and characters.
        """
        num_lines = input_text.count('\n') + 1
        words = re.findall(r'\b\w+\b', input_text)
        num_words = len(words)
        num_chars = len(input_text)
        return num_lines, num_words, num_chars

    def wordFrequency(self, input_text: str) -> Dict[str, int]:
        """
        Counts the frequency of each word in the input text.
        Returns a dictionary with words as keys and their frequency as values.
        """
        words = re.findall(r'\b\w+\b', input_text.lower())
        self.word_freq = Counter(words)
        self.total_words = sum(self.word_freq.values())
        return self.word_freq

    def letterFrequency(self, input_text: str) -> Dict[str, int]:
        """
        Counts the frequency of each letter in the input text.
        Returns a dictionary with letters as keys and their frequency as values.
        """
        letters = re.findall(r'[a-zA-Z]', input_text.lower())
        return Counter(letters)

    def frequency(self, word: str) -> float:
        """
        Returns the relative frequency of the word in the input text.
        """
        return self.word_freq[word.lower()] / self.total_words if self.total_words else 0.0

    def format_word_freq(self, word_freq: Dict[str, int]) -> str:
        """
        Formats the word frequency dictionary into a table-like string including relative frequencies.
        """
        lines = ["| Word | Count | Relative Frequency |", "|------|-------|-------------------|"]
        for word, count in sorted(word_freq.items(), key=lambda item: item[1], reverse=True):
            relative_frequency = (count / self.total_words) * 100
            lines.append(f"| {word} | {count} | {relative_frequency:.2f}% |")
        return "\n".join(lines)

    def process_file(self, filepath: str) -> str:
        """
        Processes a single file and captures the output results into a file 'ResultsOfProcessing.txt'.
        """
        result_filename = 'ResultsOfProcessing.txt'
        with open(result_filename, 'w') as result_file:
            content = self.print(filepath)
            num_lines, num_words, num_chars = self.wc(content)
            word_freq = self.wordFrequency(content)
            letter_freq = self.letterFrequency(content)

            result_file.write(f'File: {os.path.basename(filepath)}\n')
            result_file.write(f'Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}\n')
            result_file.write('Word Frequencies:\n')
            result_file.write(self.format_word_freq(word_freq))
            result_file.write('\nLetter Frequencies:\n')
            for letter, freq in sorted(letter_freq.items(), key=lambda item: item[1], reverse=True):
                result_file.write(f'{letter}: {freq}\n')
            result_file.write('\n')

        return result_filename

    def process_directory(self, directory: str) -> str:
        """
        Processes all files in the given directory and captures the output results
        into a file 'ResultsOfProcessing2.txt'.
        """
        result_filename = 'ResultsOfProcessing2.txt'
        with open(result_filename, 'w') as result_file:
            for filename in os.listdir(directory):
                filepath = os.path.join(directory, filename)
                if os.path.isfile(filepath):
                    content = self.print(filepath)
                    num_lines, num_words, num_chars = self.wc(content)
                    word_freq = self.wordFrequency(content)
                    letter_freq = self.letterFrequency(content)

                    result_file.write(f'File: {filename}\n')
                    result_file.write(f'Lines: {num_lines}, Words: {num_words}, Characters: {num_chars}\n')
                    result_file.write('Word Frequencies:\n')
                    result_file.write(self.format_word_freq(word_freq))
                    result_file.write('\nLetter Frequencies:\n')
                    for letter, freq in sorted(letter_freq.items(), key=lambda item: item[1], reverse=True):
                        result_file.write(f'{letter}: {freq}\n')
                    result_file.write('\n')

        return result_filename

if __name__ == "__main__":
    pyword = PyWordForWord()
    # Process a single file
    single_result_file = pyword.process_file('/Users/peter/Dev/PyWordForWord/testdata/testdata2.txt')
    print(f"Processing complete. Results saved to {single_result_file}")
    # Process all files in the directory
    directory_result_file = pyword.process_directory('/Users/peter/Dev/PyWordForWord/testdata')
    print(f"Processing complete. Results saved to {directory_result_file}")
