#-*- coding: utf-8 -*-
from collections import Counter, OrderedDict

def frequencies(text):
    'Get frequency of every character in the given text.'
    frequencies = Counter() 
    for word in text.split():
        frequencies[word.strip()] += 1
    return OrderedDict(frequencies.most_common())
