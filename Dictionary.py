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
                frequency = frequencies.get(word, None)
                if frequency == None:
                    frequencies[word] = 1
                else:
                    frequencies[word] = frequency + 1
        return frequencies

    def assignChars(self):
        # ASCII [33, ..., 202]
        dictionary = dict()
        charcode = 33 # ASCII code
        for key in self._sortedwords:
            if charcode < 203:
                dictionary[key] = chr(charcode)
            else:
                charcode = 0
            charcode += 1

        return dictionary


    def getfilename(self):
        return self._filename

    def getfrequencies(self):
        return self._frequencies

    def getsortedwords(self):
        return self._sortedwords

    def getdictionary(self):
        return self._dictionary