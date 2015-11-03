class Dictionary:

    def __init__(self, file_name):
        # The dictionary will read the string from a text file, so the file name must be specified
        self._filename = file_name
        self._frequencies = self.countWords()
        self._sortedwords = sorted(self._frequencies, key=self._frequencies.get, reverse=True)
        self._dictionary = self.assignChars() # ASCII assignation

    def countWords(self):
        # Method for counting the words in the specified file
        f = open(self._filename, 'r')
        frequencies = dict()
        for line in f:
            for word in line.split(" "):
                word = word.rstrip('\n') #.lower() Add to count lower case and upper case as the same word
                frequency = frequencies.get(word, None)
                if frequency == None:
                    frequencies[word] = 1
                else:
                    frequencies[word] = frequency + 1
        return frequencies

    def assignChars(self):
        # ASCII [33, ..., 202]
        dictionary = dict()
        # code word = secondprefix + firstprefix + charcode
        firstprefix = 0
        use_firstprefix = False
        secondprefix = 0
        use_secondprefix = False
        charcode = 33 # ASCII code
        for key in self._sortedwords:

            if charcode == 203:
                charcode = 33
                use_firstprefix = True

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

    def getsortedwords(self):
        return self._sortedwords

    def getdictionary(self):
        return self._dictionary