import unittest, os
from .context import module

class StopWordsTestCase(unittest.TestCase):
    """Tests for `StopWords.py`."""

    def test_filter_stop_words(self):
        """Should succefully filter stopwords from a list of words"""
        words = ['Hi', 'I', 'am', 'going', 'very', 'well', 'today']
        words_without_stopwords = ['Hi', 'going', 'today']
        stopwords_filename = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data', 'stopWords', 'stop-words_EN.txt'))
        stopwords = module.StopWords(stopwords_filename)
        self.assertTrue(stopwords.filter_stopwords(words) == words_without_stopwords)

if __name__ == '__main__':
    unittest.main()
