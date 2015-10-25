class Dictionary:

    def __init__(self, file_name):
        self._filename = file_name
        self._frequencies = self.countWords()
        self._sortedwords = sorted(self._frequencies, key=self._frequencies.get, reverse=True)

    def countWords(self):
        f = open(self._filename, 'r')
        frequencies = dict()
        for line in f:
            for word in line.split():
                frequency = frequencies.get(word, None)
                if frequency == None:
                    frequencies[word] = 1
                else:
                    frequencies[word] = frequency + 1
        return frequencies

    def getfilename(self):
        return self._filename

    def getfrequencies(self):
        return self._frequencies

    def getsortedwords(self):
        return self._sortedwords
