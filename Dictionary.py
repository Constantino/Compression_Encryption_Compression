#-*- coding: utf-8 -*-
from functions import frequencies, frequencies_val
class Dictionary:
    'Dictionary to encode a given text.'

    def __init__(self, text):
        # The dictionary will read the string from a text file, so the file name must be specified
        self._original_text = text
        self._frequencies = frequencies(self._original_text)
        self._dictionary = self.assignChars() # ASCII assignation

    def get_self_compression_ratio(self,dictionary):

        freq = frequencies_val(self._original_text)
        l_key = int()
        l_value = int()

        for e in dictionary:
            l_key += len(e)*freq[e]
            l_value += len(dictionary[e])*freq[e]

        print "l_key: ",l_key," l_value: ",l_value
        return (1.0*l_key)/l_value

    def assignChars(self):
        # ASCII [33, ..., 202]
        dictionary = dict()
        # code word = secondprefix + firstprefix + charcode
        firstprefix = 0
        use_firstprefix = False
        secondprefix = 0
        use_secondprefix = False
        charcode = 33 # ASCII code
        for key in self._frequencies:

            if charcode == 205: # One more to get rid of characters 127 (delete) and 92 (\)
                charcode = 33
                use_firstprefix = True
            elif charcode == 92: # Skip character 92
                charcode = 93
            elif charcode == 127: # Skip character 127
                charcode = 128

            if firstprefix == 91:
                firstprefix = 97
            elif firstprefix == 123:
                firstprefix = 65 
                use_secondprefix = True

            if secondprefix == 91:
                secondprefix = 97
            elif secondprefix == 123:
                secondprefix = 65

            if use_firstprefix == False:
                dictionary[key] = chr(charcode)
                charcode += 1
            elif use_secondprefix == False:
                dictionary[key] = chr(firstprefix) + chr(charcode)
                charcode += 1
                firstprefix += 1
            else:
                dictionary[key] = chr(secondprefix) + chr(firstprefix) + chr(charcode)
                charcode += 1
                firstprefix += 1
                secondprefix += 1
            
        return dictionary


    def getfilename(self):
        return self._filename

    def getfrequencies(self):
        return self._frequencies

    def getdictionary(self):
        return self._dictionary


def dictionary_encoding(text, dictionary):
    nstring = ''
    dicto = dictionary.getdictionary()
    for word in text.split():
        if word in dicto:
            nstring = nstring + dicto[word] + ' '
    print "*** Dictionary: ",dicto
    with open('Results/dictionary_and_compression_ratio.txt', 'w') as f:
            string = "Dictionary: \n"
            string += str(dicto)
            string += "\n\nCompression ratio: "+str(dictionary.get_self_compression_ratio(dicto))
            f.write(string)
    return nstring


def dictionary_decoding(encoded, dictionary):
    normal_dictionary = dictionary.getdictionary()
    inverted_dictionary = {value: key for key, value in normal_dictionary.iteritems()}
    decoded_text = ''
    encoded = encoded.split(' ')[:-1]
    for word in encoded:
        decoded_text = decoded_text + inverted_dictionary[word] + ' '
    return decoded_text