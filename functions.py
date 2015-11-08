#-*- coding: utf-8 -*-
from collections import Counter

def frequencies(text):
	'Get frequency of every character in the given text.'
	frequencies = Counter()	
	for word in text.split(' '):
		frequencies[word] += 1
	return frequencies
