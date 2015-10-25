class Dictionary:

    def __init__(self, file_name):
        self._filename = file_name
        self._text = self.readFile()

    def readFile(self):
        fileInput = open(self._filename, 'r')
        text = fileInput.read()
        return text

    def countWords(self):
        frequencies = dict()
        for word in self._text:
            frequency = frequencies.get(word, None)
            if frequency == None:
                frequencies[word] = 1
            else:
                frequencies[word] = frequency + 1
        return frequencies
