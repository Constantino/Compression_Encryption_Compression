#-*- coding: utf-8 -*-
from collections import Counter, OrderedDict

def frequencies(text):
    'Get frequency of every character in the given text.'
    frequencies = Counter() 
    freq = Counter()
    len_text = len(text)
    for word in text.split():
        frequencies[word.strip()] += 1
        freq[word.strip()] += 1.0/len_text

    return OrderedDict(frequencies.most_common())

def frequencies_from_dictionary(text):
    new_text = ""
    for e in text:
        new_text += e + " "

    return frequencies(new_text)

def frequencies_val(text):
    
    freq = Counter()
    len_text = len(text)
    for word in text.split():
        freq[word.strip()] += len(word)*1.0/len_text
    
    with open('Results/dictionary_frequencies.txt', 'w') as f:
            f.write("frequencies: \n")
            f.write(str(freq))

    #check_freq(freq)
    return freq

def check_freq(freq):
    su = 0
    for e in freq:
        su += freq[e]
    print "su freq: ",su