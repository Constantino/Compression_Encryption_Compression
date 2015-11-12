#-*- coding: utf-8 -*-
from functions import frequencies
class Dictionary:
    'Dictionary to encode a given text.'

    def __init__(self, text):
        # The dictionary will read the string from a text file, so the file name must be specified
        self._original_text = text
        self._frequencies = frequencies(self._original_text)
        self._dictionary = self.assignChars() # ASCII assignation


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