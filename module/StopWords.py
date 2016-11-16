# -*- coding: utf-8 -*-
#!/usr/bin/env python3

#class StopWords is to apply function using a list of stopwords contain in a file
class StopWords:

    #stopwords_filepath is the path to a file containing a list of stopwords, one stopwords per line
    def __init__(self, stopwords_filepath):
        self.stopwords = set(map(lambda word: word.lower().strip('\n'), open(stopwords_filepath,'r')))

    #filter_stopwords remove all stopwordscontain in a list of words
    def filter_stopwords(self, words):
        return list(filter(lambda word: not word.lower() in self.stopwords, words))
